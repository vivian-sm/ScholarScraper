from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords as nltk_stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import binarize
import numpy as np

language_pack = ["en", "id"]

class ScholarComputation:
    def __init__(self, language: str = "en"):
        self.set_language(language)
        self.set_preprocessor()

    # ---------------------------------------------------------------------------------------------
    # Check Text
    # ---------------------------------------------------------------------------------------------
    @staticmethod
    def check_text(text: str):
        if not isinstance(text, str):
            raise Exception("Text must be a string")
        if not text.strip():
            raise Exception("Text cannot be empty")

    # ---------------------------------------------------------------------------------------------
    # Language Setter
    # ---------------------------------------------------------------------------------------------
    def set_language(self, language: str):
        if not isinstance(language, str):
            raise Exception("Language must be a string")
        if len(language) != 2:
            raise Exception("Language code must be 2 characters")
        if language not in language_pack:
            raise Exception("Language not supported")
        self.__language = language

    # ---------------------------------------------------------------------------------------------
    # Pre-Processing
    # ---------------------------------------------------------------------------------------------
    def pre_processor_indonesia(self):
        stemmer_factory = StemmerFactory()
        self.stemmer = stemmer_factory.create_stemmer()
        
        stopword_factory = StopWordRemoverFactory()
        self.stopword = stopword_factory.create_stop_word_remover()

    def pre_processor_english(self):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stopword = set(nltk_stopwords.words("english"))

    def set_preprocessor(self):
        if self.__language == "en":
            self.pre_processor_english()
        elif self.__language == "id":
            self.pre_processor_indonesia()

    # ---------------------------------------------------------------------------------------------
    # Case Folding
    # ---------------------------------------------------------------------------------------------
    def case_folding(self, documents):
        if isinstance(documents, list):
            for doc in documents:
                self.check_text(doc)
            return [doc.lower() for doc in documents]
        else:
            raise Exception("Documents must be string or list of strings")
    
    # ---------------------------------------------------------------------------------------------
    # Stemming
    # ---------------------------------------------------------------------------------------------
    def stemming(self, documents):
        if isinstance(documents, list):
            return [self.stemmer.stem(doc) for doc in documents]
        return self.stemmer.stem(documents)

    # ---------------------------------------------------------------------------------------------
    # Lemmatization
    # ---------------------------------------------------------------------------------------------
    def lemmatization(self, text):
        if isinstance(text, list):
            return [self.lemmatization(t) for t in text]

        self.check_text(text)
        if self.__language == "en":
            return self.lemmatizer.lemmatize(text)
        elif self.__language == "id":
            return self.stemmer.stem(text)

    # ---------------------------------------------------------------------------------------------
    # Stopword Removal
    # ---------------------------------------------------------------------------------------------
    def stopword_removal_indonesia(self, text: str):
        return self.stopword.remove(text)

    def stopword_removal_english(self, text: str):
        words = text.split()
        filtered_words = [w for w in words if w.lower() not in self.stopword]
        return " ".join(filtered_words)

    def stopword_removal(self, documents):
        if isinstance(documents, list):
            return [self.stopword_removal(doc) for doc in documents]
        self.check_text(documents)
        if self.__language == "en":
            return self.stopword_removal_english(documents)
        elif self.__language == "id":
            return self.stopword_removal_indonesia(documents)

    # ---------------------------------------------------------------------------------------------
    # Feature Weighting (TF-IDF)
    # ---------------------------------------------------------------------------------------------
    def train_tfidf_weighting(self, documents):
        self.vectorizer = CountVectorizer()
        count_matrix = self.vectorizer.fit_transform(documents)
        self.tfidf_transformer = TfidfTransformer()
        tfidf_matrix = self.tfidf_transformer.fit_transform(count_matrix)
        self.set_vectorizer_vocabulary(tfidf_matrix)
        return tfidf_matrix


    def apply_tfidf_weighting(self, documents):
        if self.vectorizer is None or self.tfidf_transformer is None:
            raise RuntimeError(
                "TF-IDF model not trained. Call train_tfidf_weighting() first."
            )
        count_matrix = self.vectorizer.transform(documents)
        tfidf_matrix = self.tfidf_transformer.transform(count_matrix)
        return tfidf_matrix

    def set_vectorizer_vocabulary(self,tfidf_matrix,method = "mean", top_n=10):
        if self.vectorizer is None:
            raise RuntimeError(
                "TF-IDF model not trained. Call train_tfidf_weighting() first."
            )
        self.vocabulary = self.vectorizer.get_feature_names_out().tolist()
        
        if method == "mean":
            computed_word = np.asarray(tfidf_matrix.mean(axis=0)).ravel()
        elif method == "sum":
            computed_word = np.asarray(tfidf_matrix.sum(axis=0)).ravel()
        
        top_indices = computed_word.argsort()[::-1][:top_n]
        self.top_word = [
            (self.vocabulary[i], computed_word[i])
            for i in top_indices
        ]
    
    # ---------------------------------------------------------------------------------------------
    # Similarity Measures
    # ---------------------------------------------------------------------------------------------
    def calculate_similarity(self, query, documents):
        if query.shape[1] != documents.shape[1]:
            raise Exception("Query and documents vector size mismatch")
        similarities = cosine_similarity(query, documents)
        return similarities.flatten()

        
