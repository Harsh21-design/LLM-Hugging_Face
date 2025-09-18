from transformers import pipeline

text_gen = pipeline("text-generation", model="gpt2")

prompt = "what is beauty?"

response = text_gen(prompt, 
                    max_new_tokens = 40,
                    truncation=True)

print("Generated Text:",response[0]['generated_text'])