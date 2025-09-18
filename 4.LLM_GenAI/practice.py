# pip install transformers kernels torch(in terminal)
from transformers import pipeline

# Using Text-Generation Pipeline
gentext = pipeline("text-generation", model="gpt2")

gentext("AI & Automation is")

gentext(
    "What is chatgpt?",
    max_length = 20,
    num_return_sequences = 2, #number of sentences
    )

# Using Sentiment-Analysis pipeline
classifier = pipeline("sentiment-analysis")

classifier("I love to play video games")

mysentiments = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
    )

mysentiments("Aaj mujhe khana bnana pdega")
