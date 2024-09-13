from speech_recognition_custom import recognize_speech
from lyrics import complete_lyric
from utils import show_popup

def main():
    text = recognize_speech()
    if text:
        artist, title, completed_lyric = complete_lyric(text)
        show_popup(text, artist, title, completed_lyric)

if __name__ == "__main__":
    main()