import os
from google.cloud import texttospeech
import pygame

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret.json"

client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.SynthesisInput(text="私がチャンピオンだ。")

voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

filename = "output2.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f'Audio content written to file "{filename}"')

pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

gender_type = {
    "default": texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    "male": texttospeech.SsmlVoiceGender.MALE,
    "female": texttospeech.SsmlVoiceGender.FEMALE,
    "neutral": texttospeech.SsmlVoiceGender.NEUTRAL,
}