######################################################################
############   Text processing   #####################################
######################################################################

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):
    '''
    text: str
    returns a preprocessed, lemmatized string
    Operations: punctuation, digits, stopwords removed; lower; lemmatizer
    '''
    for punctuation in string.punctuation:
        text = text.replace(punctuation,'')
    text = text.lower()
    text = ''.join(char for char in text if not char.isdigit())

    stop = set (stopwords.words('english'))
    tokens = word_tokenize(text)
    text =  " ".join([word for word in tokens if word not in stop])

    lemmatizer = WordNetLemmatizer()
    text = ''.join([lemmatizer.lemmatize(word) for word in text])

    return text
