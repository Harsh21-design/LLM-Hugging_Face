from datasets import load_dataset

# data = load_dataset("stanfordnlp/imdb")
# print(data)

data = load_dataset("stanfordnlp/imdb", split="train")

# first row
# print(data[0])
# last row
# print(data[-1])

# rows between 10 and 21
# print(data[10:21])


print(" --- Printing 10 Sample Reviews from the Stanford NLP IMDb dataset --- ")
for i in range(25,36):
    print(f"Sample {i}:")
    print("Text:",data[i]['text'])
    print("Label:",data[i]['label'])
    print("\n")
    print("*"*20)
    print("\n")