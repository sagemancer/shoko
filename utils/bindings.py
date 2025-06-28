"""
Bindings for all supported games, emulators, consoles, etc.
"""

# Set the game here to include custom bindings (leave empty for the basic bindings such as movement, inventory, etc.)
SET_GAME = "Resident Evil 3 Remake"

# Generic bindings for most games
PC_BINDINGS = {
    # Shared bindings
    "up": "w",
    "left": "a",
    "down": "s",
    "right": "d",
    "jump": "space",
    "reload": "r",
    "inventory": "tab",
    "attack": "left",
    "interact": "e",
    "pause": "escape",

    # Fallout 4
    # "reload_f4": "r",
    # "console": "`",
    # "inventory_f4": "tab",
    # "interact_f4": "e",
    "skip_f4": "t",
    "kill": "",

    # Resident Evil 3 Remake
    # "skip_re3r": "escape", # Requires 2 actions for RE3R to skip a cutscene (esc+space (check PC_BINDINGS["jump"]))
}
