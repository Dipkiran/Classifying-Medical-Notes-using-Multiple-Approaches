import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')

class PreProcess():
    def __init__(self, df):
        self.df = df

    def preprocess_dataset(self):
        self.df["medical_abstract"] = self.df["medical_abstract"].apply(self.clean_text)
        self.df["medical_abstract"] = self.df["medical_abstract"].apply(self.preprocess_text)
        return self.df

    def clean_text(self, t):
        t = str(t).lower()
        t = re.sub(r'[^a-z0-9\s\-.,]', ' ', t)
        t = re.sub(r'\s+', ' ', t).strip()
        return t
    
    def preprocess_text(self, text):
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english')).union(
            {'patient', 'doctor', 'report', 'normal', 'exam'}
        )
        tokens = nltk.word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalpha()]  # remove punctuation/numbers
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

        return " ".join(tokens)