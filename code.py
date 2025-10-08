print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
layers = Layers()
keyboard.extensions.append(MediaKeys())

from kmk.modules.encoder import EncoderHandler

# Rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

# encoder volume control
encoder_handler.pins = ((board.GP28, board.GP27, board.GP26, False, 4),)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.MUTE),)]

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)    # try D5 on Feather, keeboar
keyboard.col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.tap_time = 250
keyboard.debug_enabled = False


# Make this for better looking formatting...
______ = KC.NO

keyboard.keymap = [
   [KC.ESC,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.PSCR,    KC.BRID,    KC.BRIU,     KC.MPRV,     KC.MPLY,    KC.MNXT,     KC.DEL,    KC.VOLD,    KC.MUTE,    KC.VOLU,    ______,
    KC.GRV,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,     KC.N9,     KC.N0,     KC.MINS,    KC.EQL,    KC.BSPC,    KC.NUM,     KC.PSLS,    KC.PAST,
    KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,      KC.O,      KC.P,      KC.LBRC,    KC.RBRC,   KC.BSLS,    KC.N7,      KC.N8,      KC.PMNS,
    KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,      KC.L,      KC.SCLN,   KC.QUOT,    KC.ENT,    KC.N4,      KC.N5,      KC.N6,      KC.N9,
    KC.LSFT,   KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,   KC.DOT,    KC.SLSH,   KC.RSFT,    KC.UP,     KC.N1,      KC.N2,      KC.N3,      KC.PPLS,
    KC.LCTL,   KC.LGUI,  KC.LALT,  ______,   ______,   KC.SPC,   ______,   ______,   KC.RGUI,   KC.RALT,   KC.RCTL,   KC.LEFT,   KC.DOWN,    KC.RGHT,    KC.N0,      KC.PDOT,    KC.PENT,
   ]
]

if __name__ == '__main__':
    keyboard.go()   
