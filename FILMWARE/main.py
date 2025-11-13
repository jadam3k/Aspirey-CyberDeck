from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import MatrixScanner
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# --- KONFIGURACJA PINÓW ---
keyboard.col_pins = (
    keyboard.board.GP16,  # COL1
    keyboard.board.GP17,  # COL2
    keyboard.board.GP18,  # COL3
    keyboard.board.GP19,  # COL4
    keyboard.board.GP20,  # COL5
    keyboard.board.GP21,  # COL6
    keyboard.board.GP22,  # COL7
    keyboard.board.GP0,   # COL8
    keyboard.board.GP1,   # COL9
    keyboard.board.GP2,   # COL10
    keyboard.board.GP3,   # COL11
    keyboard.board.GP4,   # COL12
    keyboard.board.GP5,   # COL13
    keyboard.board.GP26,  # COL14
)

keyboard.row_pins = (
    keyboard.board.GP11,  # ROW1
    keyboard.board.GP12,  # ROW2
    keyboard.board.GP13,  # ROW3
    keyboard.board.GP14,  # ROW4
    keyboard.board.GP15,  # ROW5
)

keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

# --- DODATKI ---
keyboard.extensions.append(MediaKeys())

# --- MAPA KLAWISZY (5 rzędów × 14 kolumn) ---
keyboard.keymap = [
    [  # ROW1
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL,
    ],
    [  # ROW2
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC,
    ],
    [  # ROW3
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
    ],
    [  # ROW4
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER, KC.NO,
    ],
    [  # ROW5
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PWR,
    ],
]

# --- URUCHOMIENIE ---
if __name__ == '__main__':
    keyboard.go()
