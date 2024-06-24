import os
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret.json"

client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.SynthesisInput(text="We are the champion!")

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

filename = "output1.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f'Audio content written to file "{filename}"')