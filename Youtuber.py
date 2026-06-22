# Example 1
from textblob import TextBlob

review = TextBlob("Python is useful and fun. I love to learn it.")

print(review.sentiment)


# Example 2
wrong_text = TextBlob("I lov Python. I want to lern more aboot it.")

corrected_text = wrong_text.correct()

print(f"Original Text: {wrong_text}")
print(f"Corrected Text: {corrected_text}")


# Example 3
article_text = TextBlob(
    "Python programming helps students build many useful projects, and make thing become easier."
)

noun_phrases = article_text.noun_phrases

print(f"Text:{article_text}")
print("Important noun phrases:")

for phrases in noun_phrases:
    print(f"{phrases}")