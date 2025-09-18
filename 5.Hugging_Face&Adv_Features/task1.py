from transformers import pipeline

# Default model
# classifier = pipeline("sentiment-analysis")

# classifier = pipeline("sentiment-analysis",
#                        model = "distilbert-base-uncased-finetuned-sst-2-english",
#                        return_all_scores=True)

# Searched Model(sentiment analysis on product reviews)
model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
classifier = pipeline("sentiment-analysis",
                      model=model_id)

result = classifier("I am using this milk product for such a long time.")#[{'label': '5 stars', 'score': 0.7290525436401367}]
# print(result)

result2 = classifier([
    "It is a useless thing to buy",
    "This is a ok-ok mobile product"
])
print(result2)

