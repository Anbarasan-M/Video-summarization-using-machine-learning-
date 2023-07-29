import machine_learning
from constants import AUDIO_FILE_NAME


def convert_and_generate_summary():
    print("Generating text")
    text = machine_learning.extract_text_from_audio(AUDIO_FILE_NAME)
    print("Generating Summary")
    summary = machine_learning.summarize_text(text)
    return summary