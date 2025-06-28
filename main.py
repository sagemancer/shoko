import speech_recognition as sr
import pyautogui
import time, sys
import keyboard

# Custom scripts
import utils.bindings as bindings
import utils.logging as log
import games.fallout4 as f4
import games.re3r as re3r

# A list of all supported games with custom bindings and tested
# If this list grows too large, it will most likely need to be restructured
# SUPPORTED_GAMES = ["Fallout4", "Resident Evil 3 Remake"]

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print(f"{log.APP_STATUS['INITIALIZING']} Booting up...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print(f"{log.APP_STATUS['COMPLETE']} Program Ready. Recording Active.")

    while True:
        with microphone as source:
            audio_stream = recognizer.listen(source)

        try:
            audio_str = recognizer.recognize_google(audio_stream).lower()

            # Set to something I can't imagine myself saying in any reasonable situation
            if "suck toes" in audio_str:
                print("Goodbye...")
                sys.exit(0)

            # This logic assumes generic PC bindings for most games
            for phrase in bindings.PC_BINDINGS: # All required binding verbiage across all games
                if phrase in audio_str:
                    print(f"{log.APP_STATUS['DETECTED']}: {audio_str}")

                    if bindings.SET_GAME == "Resident Evil 3 Remake":
                        keyboard.press(bindings.PC_BINDINGS[phrase])
                        time.sleep(12) # Increasing to 12 for longer strides, and due to chases
                        keyboard.release(bindings.PC_BINDINGS[phrase])
                    elif bindings.SET_GAME == "Fallout 4":
                        pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
                        pyautogui.keyDown(bindings.PC_BINDINGS["jump"])
                        pyautogui.keyUp(bindings.PC_BINDINGS["jump"])
                        time.sleep(8)
                        pyautogui.keyUp(bindings.PC_BINDINGS[phrase])
                    else:
                        if phrase in ["up", "down", "left", "right"]:
                            pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
                            time.sleep(5)
                            pyautogui.keyUp(bindings.PC_BINDINGS[phrase])
                        else:
                            pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
                            pyautogui.keyUp(bindings.PC_BINDINGS[phrase])

                    # If a set game is found, we can add custom key bindings, etc. to make it a little more enjoyable
                    if bindings.SET_GAME and phrase in ["interact", "skip", "dodge", "attack"]:
                        # This code is terrible, needs a refactor
                        if bindings.SET_GAME == "Fallout 4" and phrase in ["kill", "random", "skip", "interact", "skip", "dodge", "attack"]:
                            f4.custom_fallout4_bindings(audio_str)
                        elif bindings.SET_GAME == "Resident Evil 3 Remake":
                            re3r.custom_re3r_bindings(audio_str)

                    break
            else:
                print(f"{log.APP_STATUS['NOT DETECTED']}: {audio_str}")

        except sr.UnknownValueError:
            print(f"{log.APP_STATUS['TRY AGAIN']}: Unable to process speech")

if __name__ == '__main__':
    main()
