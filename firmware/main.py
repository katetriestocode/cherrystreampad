import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.OLED import OLED

keyboard = KMKKeyboard()
macros = Macros()
media_keys = MediaKeys()
encoder_handler = RotaryEncoderHandler()

#keybinds for shortcuts (to configure in puter)
OPEN_DISCORD = KC.LCTL(KC.LALT(KC.LSFT(KC.D)))
OPEN_OBS = KC.LCTL(KC.LALT(KC.LSFT(KC.C)))
OPEN_APP = KC.LCTL(KC.LALT(KC.LSFT(KC.E)))

#keyextensions
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(macros)
keyboard.extensions.append(oled)
keyboard.extensions.append(rgb)


oled = OLED(
    oled_addr = 0x3C,
    to_display="",
    i2c_sda = board.GP27,
    i2c_scl= board.GP28,
)

# Encoder Rotation: CW = Vol Up, CCW = Vol Down
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),), 
]

rgb = RGB(pixel_pin=board.GP26, num_pixels=2)

PINS = [board.GP1, board.GP2, board.GP0, board.GP6, board.GP7, board.GP29, board.GP4]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False,
)

#keymap
keyboard.keymap = [
    [
    KC.MEDIA_PLAY_PAUSE
    KC.MEDIA_NEXT_TRACK
    KC.MEDIA_PREV_TRACK
    KC.AUDIO_MUTE
    KC.OPEN_DISCORD
    KC.OPEN_OBS
    KC.OPEN_APP
    ]
]

if __name__=="__main__":
    keyboard.go()