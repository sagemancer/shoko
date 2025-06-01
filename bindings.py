"""
Bindings for all supported games, emulators, consoles, etc.
"""


"""
Game Boy based games. This should work with GBA, GBC, etc. or any other emulator with the same bindings.
"""

GB_EMU_BINDINGS = [
    "up", "down", "left",
    "right", "b", "a",
    "select", "start"
]

PC_BINDINGS = {
    "up": "W",
    "left": "A",
    "down": "S",
    "right": "D",
    "console": "`",
    "jump": "Space",
}
