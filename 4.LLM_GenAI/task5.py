import os
import json
from groq import Groq
from dotenv import load_dotenv

# api load
load_dotenv()
api_key = os.environ["GROQ_API_KEY"]

# api call
client = Groq(
    api_key = api_key
)

# Chat-bot with Conversational Memory
conversation = [] # empty conversation list
while True:
    input_prompt = input("You: ")
    if input_prompt.lower() in ["exit","quit","bye"]:
        break
    
    conversation.append({"role":"user","content":input_prompt}) #add user input in conversation list

    ai_response = client.chat.completions.create(
        messages = conversation,
        model = "llama-3.3-70b-versatile"
    )
    reply = ai_response.choices[0].message.content.strip() 
    
    print(f"AI chatbot: {reply}")
    print("*"*50)

    conversation.append({"role":"assistant","content":reply}) #add ai response in conversation list

# Basic chat-bot(no memory)
# while True:
#     input_prompt = input("You: ")
#     if input_prompt.lower() in ["exit","quit","bye"]:
#         break
#     response = client.chat.completions.create(
#         messages=[
#            {
#                "role":"user",
#                "content":input_prompt
#            }
#         ],
#         model = "llama-3.3-70b-versatile"
#     )
#     reply = response.choices[0].message.content
#     print(f"AI chatbot: {reply}")
#     print("*"*50)
