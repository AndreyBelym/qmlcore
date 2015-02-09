import re

def scan(text):
	str_context = False
	escape = False
	c_comment = False
	cpp_comment = False
	begin = 0
	invalid = []
	for i in xrange(0, len(text)):
		c = text[i]
		if escape:
			escape = False
			continue

		if cpp_comment:
			if c == "\n":
				cpp_comment = False
				end = i
				invalid.append((begin, end))
				#print "cpp-comment", (begin, end), text[begin:end]
			continue

		if c_comment:
			if text[i: i + 2] == "*/":
				end = i + 2
				c_comment = False
				invalid.append((begin, end))
				#print "c-comment", begin, end, text[begin:end]
			continue

		if str_context and c == "\\":
			escape = True
			continue

		if c == "\"" or c == "'":
			str_context = not str_context
			if str_context:
				begin = i
			else:
				end = i + 1
				invalid.append((begin, end))
				#print "string at %d:%d -> %s" %(begin, end, text[begin:end])
			continue

		if str_context:
			continue

		if text[i: i + 2] == "//":
			begin = i
			cpp_comment = True

		if text[i: i + 2] == "/*":
			c_comment = True
			begin = i


	return text, invalid

id_re = re.compile(r'([a-zA-Z]\w*)\.')

def process(text, registry):
	id_set = registry.id_set
	text, invalid = scan(text)
	def replace_id(m):
		pos = m.start(0)
		name = m.group(1)
		first = text[pos - 1] != "."
		if name in id_set:
			return ("this." if first else "") + "get('%s')." %name
		else:
			return m.group(0)
	text = id_re.sub(replace_id, text)
	#print text
	return text