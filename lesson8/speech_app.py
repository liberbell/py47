import os
from google.cloud import texttospeech
import pygame

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret.json"

def synthesize_speech(text, language="Japanese", gender="default"):
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
    synthesis_input = texttospeech.SynthesisInput(text_input)

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