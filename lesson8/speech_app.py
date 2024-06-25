import os
from google.cloud import texttospeech
import pygame

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret.json"

def synthesize_speech(text_input, language="Japanese", gender="default"):
    gender_type = {
    "default": texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    "male": texttospeech.SsmlVoiceGender.MALE,
    "female": texttospeech.SsmlVoiceGender.FEMALE,
    "neutral": texttospeech.SsmlVoiceGender.NEUTRAL,
    }

    languages = {
    "Japanese": "ja-JP",
    "English" : "en-US",
    }

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text_input)

    voice = texttospeech.VoiceSelectionParams(
        language_code=languages[language], ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

language = "English"
text = "Today is the dog days."
gender = "default"

response = synthesize_speech(text, gender="female")
filename = "output4.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f'Audio content written to file "{filename}"')