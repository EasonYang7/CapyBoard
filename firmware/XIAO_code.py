# CapyBoard — XIAO RP2040 Firmware (code.py)

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Split configuration
split = Split(
    split_type=SplitType.I2C,
    split_side=SplitSide.LEFT,
    data_pin=board.SDA,  
    data_pin2=board.SCL, 
)

# Encoder handler
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.A0, board.A1, board.A2, False),    
    (board.MISO, board.SCK, board.RX, False),  
)

encoder_handler.map = [
    # Layer 0
    [
        (KC.VOLD, KC.VOLU, KC.MUTE),          
        (KC.MS_WH_UP, KC.MS_WH_DOWN, KC.MPLY), 
    ],
    # Layer 1
    [
        (KC.BRMD, KC.BRMU, KC.MUTE),        
        (KC.MPRV, KC.MNXT, KC.MPLY),           
    ],
    # Layer 2
    [
        (KC.VOLD, KC.VOLU, KC.MUTE),           
        (KC.MS_WH_UP, KC.MS_WH_DOWN, KC.MPLY), 
    ],
]

# RGB LEDs (SK6812MINI)
rgb = RGB(
    pixel_pin=board.A3,
    num_pixels=79,
    val_limit=150,
    hue_default=0,
    sat_default=255,
    val_default=80,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
    animation_speed=1,
    breathe_center=1.5,
    knight_effect_length=3,
    reverse_animation=False,
)

# Media keys
media_keys = MediaKeys()

# Modules and extensions
layers = Layers()
keyboard.modules = [split, layers, encoder_handler]
keyboard.extensions = [rgb, media_keys]

# Keymap (must match Pico exactly)
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