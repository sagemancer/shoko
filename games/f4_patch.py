import time
import bindings
import pyautogui

NPC_IDS = {
    "piper": "00002F1E"
}

F4_PHRASES = [
    "piper" # Spawns Piper
]

def run_f4_command(console_cmd: str):
    pyautogui.press(bindings.PC_BINDINGS["console"])
    time.sleep(3) # Needs to be modified and tested to find a reliable time for the console to open and close
    pyautogui.typewrite(console_cmd, interval=0)
    pyautogui.press(bindings.PC_BINDINGS["console"])

    print(f"Successfully executed: {console_cmd}")

"""
Actions designated for this specific game
"""

# player.placeatme {NPC_IDS["NPC_NAME"]}
def place_npc(npc_name: str):
    run_f4_command(f"player.placeatme {NPC_IDS[npc_name]}")
