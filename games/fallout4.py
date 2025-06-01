import time
import pyautogui
import random

# Custom scripts
import utils.bindings as bindings
import utils.logging as log

# Add your NPC here
# I'll eventually come back and add ALL NPCs in the game, but that'll take awhile
NPC_IDS = {
    "synth": "00066644",
    "swan": "00056B7C",
    "father": "0002A19A",
    "shaun": "000570C3",
    "sean": "000570C3", # The speech recognition defaults to this spelling of "Shaun", so I've added 2 for the sake of consistency
    "hancock": "00022613",
    "deathclaw": "0001DB4C",
    "nick valentine": "00002F24",
    "feral ghoul": "000758AD",
    "ms boom": "000FDA91",
    "boomer": "000AE154",
    "mole rat": "000FA89F",
    "kellog": "0009BC6C",
    "kellog mom": "000D3C9C",
    "piper": "00002F1E",
}

# NPC_NAMES = [
#     "synth", "swan", "father",
#     "shaun", "sean", "hancock",
#     "deathclaw", "nick valentine", "feral ghoul",
#     "ms boom", "boomer", "mole rat",
#     "kellog", "kellog mom", "piper",
# ]

# Add custom phrases here, including NPCs, if you want to spawn them on certain words
F4_PHRASES = [
    # Actions
    "attack", "random", "kill",
    "reload", "inventory", "interact",
    "skip",

    # NPCs
    "synth", "swan", "father",
    "shaun", "sean", "hancock",
    "deathclaw", "nick valentine", "feral ghoul",
    "ms boom", "boomer", "mole rat",
    "kellog", "kellog mom", "piper",
]

"""
Fallout 4 commands
"""

# Generates a specific NPC and places them at your location
def generate_npc(npc_name: str):
    try:
        run_command(f"player.placeatme {NPC_IDS[npc_name]}")
    except KeyError:
        print("Not an NPC. Ignoring command.")

# End all the loaded NPCs around you (even your companion)
def last_resort():
    run_command("killall")

"""
Executed the provided command within the Steam interface
"""
def run_command(console_cmd: str):
    # Open the Steam console
    pyautogui.keyDown("`")
    pyautogui.keyUp("`")

    print(f"{log.APP_STATUS['PROCESSING']} Command executing...")

    # Auto types the command in the console (spawning characters, getting items, etc.)
    for cmd in console_cmd:
        pyautogui.write(cmd, interval=0)

    # Executes the command
    pyautogui.keyDown("Enter")
    pyautogui.keyUp("Enter")

    # Close console
    pyautogui.keyDown("`")
    pyautogui.keyUp("`")

    print(f"{log.APP_STATUS['COMPLETE']} Successfully executed: {console_cmd}")

"""
Extra bindings specifically created for Fallout 4
"""
def custom_fallout4_bindings(phrase, audio_str):
    for f4_phrase in F4_PHRASES:
        if f4_phrase in audio_str:
            print(f"{log.APP_STATUS['DETECTED']}: {audio_str}")

            # Your surroundings will not survive
            if f4_phrase == "kill":
                last_resort()

            # TODO: Need test the new "keys()" addition (NPC_NAMES list is ready if this requires too much more processing)
            if f4_phrase in NPC_IDS.keys():
                generate_npc(f4_phrase)

            # Randomly spawn an NPC
            if f4_phrase == "random":
                # TODO: Need test the new "keys()" addition (NPC_NAMES list is ready if this requires too much more processing)
                npc = random.choice(NPC_IDS.keys())
                generate_npc(npc)

            if f4_phrase == "attack":
                pyautogui.mouseDown(button="left")
                time.sleep(3) # Set to 3 so if you currently have an auto weapon, it'll shoot more than 1 round
                pyautogui.mouseUp(button="left")

            # Primary actions for doing in-game mechanics
            if f4_phrase in ["reload", "inventory", "interact", "skip"]:
                pyautogui.keyDown(bindings.FALLOUT4_BINDINGS[f4_phrase])
                pyautogui.keyUp(bindings.FALLOUT4_BINDINGS[f4_phrase])

        if not f4_phrase:
            # Custom movement for Fallout 4 to prevent getting stuck too often
            pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
            pyautogui.keyDown(bindings.PC_BINDINGS["jump"])
            pyautogui.keyUp(bindings.PC_BINDINGS["jump"])
            time.sleep(5)
            pyautogui.keyUp(bindings.PC_BINDINGS[phrase])
