# CapyBoard — Pico Firmware (code.py)

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Split configuration
split = Split(
    split_type=SplitType.I2C,
    split_side=SplitSide.RIGHT,
    data_pin=board.GP0,  
    data_pin2=board.GP1,   
)

# Column pins (GPIO2-GPIO15)
keyboard.col_pins = (
    board.GP15,
    board.GP14, 
    board.GP13,  
    board.GP12, 
    board.GP11,  
    board.GP10, 
    board.GP9,  
    board.GP8,  
    board.GP7,
    board.GP6,  
    board.GP5, 
    board.GP4,  
    board.GP3,  
    board.GP2,  
)

# ─── Row pins (GPIO16-GPIO21)
keyboard.row_pins = (
    board.GP16, 
    board.GP17,  
    board.GP18, 
    board.GP19, 
    board.GP20, 
    board.GP21,  
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Modules
layers = Layers()
media_keys = MediaKeys()
keyboard.modules = [split, layers, media_keys]

# Keymap
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    # Layer 0 Base QWERTY
    [
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, XXXXXXX, KC.ENT,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX, XXXXXXX, KC.RSFT,
        KC.LCTL,  KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, XXXXXXX, KC.SPC,  XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.APP,  XXXXXXX, KC.RCTL,
        KC.MO(1), KC.F1,   KC.F2,   KC.F3,   XXXXXXX, KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
    ],
    # Layer 1 Function
    [
        KC.GRV,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,
        _______,  _______, KC.UP,   _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,  KC.LEFT, KC.DOWN, KC.RGHT, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ],
    # Layer 2 Media
    [
        _______, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPRV, KC.MPLY, KC.MNXT, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ],
]

if __name__ == '__main__':
    keyboard.go()