# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# # api_url = "https://router.huggingface.co/hf-inference/models/HuggingFaceTB/SmolLM3-3B"
# api_url = "https://api-inference.huggingface.co/models/gpt2"

# api_token = os.environ["HUGGING_FACE_API"]

# prompt = "Tell me something about AI"

# headers = {
#     "Authorization":f"Bearer {api_token}",
#     "Content-Type":"application/json"
# }

# payload = {
#     "inputs":prompt,
#     "parameters":{
#         "max_new_tokens":20
#     }
# }

# response = requests.post(url=api_url,headers=headers,json=payload)

# if response.status_code == 200:
#     result = response.json()
#     print(result[0]["generated_text"])
# else:
#     print(f"Error:{response.status_code}")


# METHOD - 2
import os
from huggingface_hub import InferenceClient

os.environ["HUGGING_FACE_API"] = "put your api key"

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HUGGING_FACE_API"],
)

completion = client.chat.completions.create(
    # model = "llama-3.3-70b-versatile",  
    model = "meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "What is happiness?"}
    ],
    max_tokens=50
)
print(completion.choices[0].message["content"])