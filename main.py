import speech_recognition as sr
import pyautogui
import bindings
import games.f4_patch


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("[WAIT] Booting up...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print("[READY] Begin speaking...")

    while True:
        with microphone as source:
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"Unrecognized: {text}")

            for f4_phrase in games.f4_patch.F4_PHRASES:
                if f4_phrase in text:
                    print(f"Recognized: {text}")
                    games.f4_patch.place_npc("piper")

            if f4_phrase not in text:
                for phrase in bindings.PC_BINDINGS:
                    if phrase in text:
                        print(f"Recognized: {text}")
                        pyautogui.press(bindings.PC_BINDINGS[phrase])
        
        except sr.UnknownValueError:
            print("Unable to process speech. Try again.")
        except sr.RequestError as e:
            print(f"Unable to communicate with speech recognition service.\n{e}")

if __name__ == '__main__':
    main()
