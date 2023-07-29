import whisper
from transformers import pipeline


def extract_text_from_audio(audio_file_name):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file_name)
    file = open("text.txt", "w")
    file.write(result['text'])
    print(result)
    return result['text']


def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
