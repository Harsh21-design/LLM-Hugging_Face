import gradio as gr
from transformers import pipeline

model = "openai/whisper-base"
pipe = pipeline("automatic-speech-recognition", model=model)

def voice_to_text(audio):
  result = pipe(audio)
  return result["text"]


app = gr.Interface(
    fn = voice_to_text,
    inputs = gr.Audio(sources=["microphone","upload"],type="filepath"),
    outputs = ['text'],
    title = 'Voice-To-Text Generation App',
    description = 'Transcribes audio into text using Whisper-base AI model'
)  

if __name__ == "__main__":
   app.launch()