def on_forever():
    basic.show_icon(IconNames.DIAMOND)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_DIAMOND)
basic.forever(on_forever)
