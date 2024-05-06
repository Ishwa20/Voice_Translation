import speech_recognition
import gtts
import playsound
from googletrans import Translator

# Define a dictionary of language codes and their corresponding language names
language_codes = {
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
    "ar": "Arabic",
    "bn": "Bengali",
    "zh-CN": "Chinese (Simplified)",
    "zh-TW":"Chinese (Traditional)",
    "nl": "Dutch",
    "tl": "Filipino",
    "fr": "French",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "hu": "Hungraian",
    "is": "Icelandic",
    "id": "Indonesian",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "kn":"Kannada",
    "ko": "Korean",
    "la": "Latin",
    "mg": "Malagasy",
    "ml": "Malayalam",
    "mr": "Marathi",
    "mn": "Mongolian",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "no": "Norwegian",
    "or": "Odia (Oriya)",
    "pl": "Polish",
    "pt": "Portuguese",
    "pa": "Punjabi",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "sd": "Sindhi",
    "su": "Sundanese",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "tk": "Turkmen",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zu": "Zulu",
    # Add more languages as needed
}

# Prompt the user to select input language
print("Select input language:")
for code, name in language_codes.items():
    print(f"{code}: {name}")

input_lang = input("Enter input language code: ")

# Prompt the user to select output language
print("\nSelect output language:")
for code, name in language_codes.items():
    print(f"{code}: {name}")

output_lang = input("Enter output language code: ")

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("\nSpeak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language=input_lang)
    print("Input Text:", text)

translator = Translator()
translation = translator.translate(text, dest=output_lang)
print("Translated Text:", translation.text)

converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")