# Example 3
from textblob import TextBlob

article_text = TextBlob(
    "Python programming helps students build many useful projects, and make thing become easier."
)

noun_phrases = article_text.noun_phrases

print(f"Text:{article_text}")
print("Important noun phrases:")

for phrases in noun_phrases:
    print(f"{phrases}")