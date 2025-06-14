import re
import pandas as pd
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Download nltk resources 
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

# POS Tag conversion for lemmatization
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Basic stopwords
EN_STOPWORDS = set(stopwords.words('english'))

# Define basic lemmatizer
lemmatizer = WordNetLemmatizer()

# Text cleaner
def clean_sentence(text):
    # Lowercase, remove punctuation and digits
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [t for t in tokens if t not in EN_STOPWORDS and len(t) > 2]
    
    # POS tagging and lemmatization
    pos_tags = pos_tag(tokens)
    lemmas = [lemmatizer.lemmatize(t, get_wordnet_pos(pos)) for t, pos in pos_tags]
    
    return ' '.join(lemmas)

# Apply preprocessing to a DataFrame
def preprocess_text(df, col='sentence'):
    df['clean_sentence'] = df[col].apply(clean_sentence)
    return df