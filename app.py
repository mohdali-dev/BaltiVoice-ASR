import gradio as gr
from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    model="mohdali1/whisper-small-balti",
    generate_kwargs={"language": "urdu", "task": "transcribe"}
)

def transcribe(audio):
    if audio is None:
        return "Please record or upload audio."
    result = asr(audio)
    return result["text"]

demo = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources=["microphone", "upload"], type="filepath"),
    outputs=gr.Textbox(label="Balti Transcription", rtl=True),
    title="🎙️ BaltiVoice ASR",
    description="""
**First AI-powered Speech Recognition system for Balti language**

Balti (بلتی) is a low-resource Tibetic language spoken in Gilgit-Baltistan, Pakistan.
Record or upload Balti audio → transcription appears in native Balti script.

*Fine-tuned Whisper-small on 16.8 hours of validated speech | WER: 30%*
    """,
    theme=gr.themes.Soft()
)

demo.launch()
