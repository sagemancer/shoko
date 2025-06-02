import time
import pyautogui
import keyboard

# Custom scripts
import utils.bindings as bindings
import utils.logging as log

# NOTE: Currently, only voice controls are included. Nothing has been added to change the game

RE3R_PHRASES = [
    # Actions
    "attack", "reload", "inventory",
    "interact", "skip",
]

"""
Extra bindings specifically created for Fallout 4
"""
def custom_re3r_bindings(audio_str):
    for re3r_phrase in RE3R_PHRASES:
        if re3r_phrase in audio_str:

            if re3r_phrase == "attack":
                pyautogui.mouseDown(button="right")
                pyautogui.mouseDown(button="left")
                time.sleep(3) # Set to 3 so if you currently have an auto weapon, it'll shoot more than 1 round
                pyautogui.mouseUp(button="left")
                pyautogui.mouseUp(button="right")

            if re3r_phrase in ["pause", "skip"]:
                keyboard.send(bindings.PC_BINDINGS["pause"])

            if re3r_phrase == "dodge":
                keyboard.send(bindings.PC_BINDINGS["jump"])

            if re3r_phrase == "interact":
                pyautogui.mouseDown(button="left")
                pyautogui.mouseUp(button="left")

            # Shared phrases across all games
            if re3r_phrase in ["reload", "inventory"]:
                keyboard.send(bindings.PC_BINDINGS[re3r_phrase])
