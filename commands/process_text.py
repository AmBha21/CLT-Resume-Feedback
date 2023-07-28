import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)  # Remove digits
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text
