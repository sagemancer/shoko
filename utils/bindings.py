"""
Bindings for all supported games, emulators, consoles, etc.
"""

# Generic bindings for most games
PC_BINDINGS = {
    "up": "w",
    "left": "a",
    "down": "s",
    "right": "d",
    "jump": "space",
}

"""
These bindings assume the default bindings are present
"""

FALLOUT4_BINDINGS = {
    # "console": "`",
    "reload": "r",
    "inventory": "tab",
    "interact": "e",
    "skip": "t",
}

RE3R_BINDINGS = {
    "reload": "r",
    "inventory": "tab",
    "interact": "f",
    "skip": "escape", # Requires 2 actions to skip a cutscene (esc+space (check PC_BINDINGS["jump"]))
}
