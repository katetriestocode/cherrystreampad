import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.OLED import OLED

keyboard = KMKKeyboard()
macros = Macros()
media_keys = MediaKeys()
encoder_handler = RotaryEncoderHandler()

#keybinds for shortcuts (to configure in puter)
OPEN_DISCORD = KC.LCTL(KC.LALT(KC.LSFT(KC.D)))
OPEN_OBS = KC.LCTL(KC.LALT(KC.LSFT(KC.C)))


oled = OLED(
    oled_addr = 0x3C,
    to_display="",
    i2c_sda = board.GP27,
    i2c_scl= board.GP28,
)

rgb = RGB(pixel_pin=board.GP26, num_pixels=2)


#keyextensions
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(macros)
keyboard.extensions.append(oled)
keyboard.extensions.append(rgb)



encoder = RotaryEncoderHandler(pin_a=board.GP3, pin_b=board.GP4)
encoder.rotation_cw = KC.VOLU 
encoder.rotation_ccw = KC.VOLD 
keyboard.modules.append(encoder)



PINS = [board.GP1, board.GP2, board.GP0, board.GP6, board.GP7, board.GP29]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False,
)

#keymap
keyboard.keymap = [
    [
    KC.AUDIO_MUTE
    OPEN_DISCORD
    OPEN_OBS
    KC.MEDIA_PLAY_PAUSE
    KC.MEDIA_NEXT_TRACK
    KC.MEDIA_PREV_TRACK
    ]
]

if __name__=="__main__":
    keyboard.go()