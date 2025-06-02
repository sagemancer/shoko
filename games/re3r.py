import time
import pyautogui
import random

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
def custom_re3r_bindings(phrase, audio_str):
    for re3r_phrase in RE3R_PHRASES:
        if re3r_phrase in audio_str:
            print(f"{log.APP_STATUS['DETECTED']}: {audio_str}")

            if re3r_phrase == "attack":
                with pyautogui.mouseDown(button="right"):
                    pyautogui.mouseDown(button="left")
                    time.sleep(3) # Set to 3 so if you currently have an auto weapon, it'll shoot more than 1 round
                    pyautogui.mouseUp(button="left")
                
                pyautogui.mouseUp(button="right")

            if re3r_phrase == "skip":
                pyautogui.keyDown(bindings.RE3R_BINDINGS[re3r_phrase])
                pyautogui.keyUp(bindings.RE3R_BINDINGS[re3r_phrase])
                pyautogui.keyDown(bindings.PC_BINDINGS["jump"])
                pyautogui.keyUp(bindings.PC_BINDINGS["jump"])

            if re3r_phrase == "dodge":
                pyautogui.keyDown(bindings.PC_BINDINGS["jump"])
                pyautogui.keyUp(bindings.PC_BINDINGS["jump"])

            if re3r_phrase in ["reload", "inventory", "interact"]:
                pyautogui.keyDown(bindings.RE3R_BINDINGS[re3r_phrase])
                pyautogui.keyUp(bindings.RE3R_BINDINGS[re3r_phrase])

        if not re3r_phrase:
            pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
            time.sleep(5)
            pyautogui.keyUp(bindings.PC_BINDINGS[phrase])
