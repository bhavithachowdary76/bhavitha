# -*- coding: utf-8 -*-
"""Day9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rvKiF_A5pWwTLLxAa8eGycnT_DvBFsvf
"""

import gensim
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string, strip_punctuation, strip_numeric
from gensim.utils import simple_preprocess
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Preprocessing function
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove stopwords using Gensim
    text = remove_stopwords(text)

    # Tokenize using Gensim's simple_preprocess
    tokens = simple_preprocess(text, deacc=True)  # deacc=True removes punctuation

    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token, wordnet.VERB) for token in stemmed_tokens]

    # Remove any additional stopwords
    final_tokens = [word for word in lemmatized_tokens if word not in stop_words]

    return final_tokens

# Process text from a file
def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            processed_tokens = preprocess_text(text)
            return processed_tokens
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

# Example usage
if __name__ == "__main__":
    file_path = "sample_text.txt"  # Replace with your file path
    processed_tokens = process_file(file_path)
    print("Processed Tokens:")
    print(processed_tokens)