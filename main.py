import speech_recognition as sr
import pyautogui
import time

# Custom scripts
import utils.bindings as bindings
import utils.logging as log
import games.fallout4 as f4

# A list of all supported games with custom bindings and tested
# If this list grows too large, it will most likely need to be restructured
SUPPORTED_GAMES = ["Fallout4"]

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
            print(f"{log.APP_STATUS['NOT DETECED']}: {audio_str}")

            for game in SUPPORTED_GAMES:
                # Add a list on GitHub of all supported games
                set_game = input("Set Your Game: \nA full list is available here: https://github.com/sagemancer/shoko")

            # This logic assumes generic PC bindings for most games
            """
            W = Forward
            A = Left
            S = Down
            D = Right
            Space = Jump
            """
            for phrase in bindings.PC_BINDINGS:
                if phrase in audio_str:
                    print(f"{log.APP_STATUS['DETECTED']}: {audio_str}")

                    # If a set game is found, we can add custom key bindings, etc. to make it a little more enjoyable
                    if set_game:
                        if set_game in ["Fallout4", "Fallout 4"]:
                            f4.custom_fallout4_bindings(phrase, audio_str)
                    else:
                        pyautogui.keyDown(bindings.PC_BINDINGS[phrase])
                        time.sleep(5)
                        pyautogui.keyUp(bindings.PC_BINDINGS[phrase])

        except sr.UnknownValueError:
            print("Unable to process speech. Try again.")

if __name__ == '__main__':
    main()
