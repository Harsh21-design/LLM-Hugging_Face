# app.py file 
import gradio as gr
from transformers import pipeline

generatetext = pipeline("text-generation", model="distilgpt2")

def textgen(prompt):
    response =  generatetext(prompt, 
                    max_new_tokens = 80,
                    truncation=True)
    return response[0]['generated_text']


text_gen_space = gr.Interface(
    fn = textgen,
    inputs = ['text'],
    outputs = ['text'],
    title = 'AI Text Generation Gradio App'
)  

text_gen_space.launch()

# requirements.txt
# transformers
# torch




# BASIC GRADIO APP
# def greet(name):
#     return "Hello " + name + "!"

# demo = gr.Interface(
#     fn=greet,
#     inputs = ['text'],
#     outputs = ['text'],
#     title = "Gradio Greeting App"
# )

# demo.launch()