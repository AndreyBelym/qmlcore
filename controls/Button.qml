 Rectangle {
     id: button;
     event triggered;

     width: 145; height: 60;
     color: "blue";
     smooth: true;
     radius: 9;
     focus: true;
     property alias text: label.text;
     border { color: "#B9C5D0"; width: 1; }

     color: activeFocus? "purple": "blue";
     opacity: activeFocus? 1: 0.3;
     Behavior on opacity	{ Animation { duration: 1000; } }
     Behavior on color		{ ColorAnimation { duration: 1000; } }

/*
     gradient: Gradient {
         GradientStop {color: "#CFF7FF"; position: 0.0; }
         GradientStop {color: "#99C0E5"; position: 0.57; }
         GradientStop {color: "#719FCB"; position: 0.9; }
     }

*/
     Text {
         id: label;
         anchors.centerIn: parent;
         font.pointSize: 12;
         color: "white";
     }

     MouseArea {
         anchors.fill: parent;
         onClicked: { button.triggered(); }
     }

     onSelectPressed: { this.triggered(); }
     onTriggered: { console.log(button.text + " triggered"); }
 }