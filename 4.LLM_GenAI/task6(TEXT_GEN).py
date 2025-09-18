from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

prompt = "What is Space ?"

inputs = tokenizer(prompt,return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_new_tokens=20)

print(tokenizer.decode(outputs[0]))