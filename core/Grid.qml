Layout {
	property int maxWidth: 1000;

	onWidthChanged: { this._delayedLayout.schedule() }
}
