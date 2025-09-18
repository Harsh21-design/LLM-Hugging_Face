import os
from groq import Groq

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]

client = Groq(
    api_key = api_key
)

prompt_template = "Explain {concept} in one {style} sentence or line."
variations = [
    {"concept":"Data science","style":"simple"},
    {"concept":"Biology","style":"formal"},
    {"concept":"Maths","style":"technical"},
    {"concept":"Computers","style":"funny"}
]

for variation in variations:
    prompt = prompt_template.format(concept = variation["concept"], style = variation["style"])
    chat_completion = client.chat.completions.create(
        messages=[
           {
               "role":"user",
               "content":prompt
           }
        ],
        model = "llama-3.3-70b-versatile"
    )
    generated_text = chat_completion.choices[0].message.content
    print(f"Prompt: {prompt}")
    print(f"Response: {generated_text}")
    print("\n")