import time
from models.scholarComputation import ScholarComputation as sc

def timed(label, func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"{label}: {(end - start):.6f} seconds")
    return result


if __name__ == "__main__":
    # =============================================================================================
    # ENGLISH TEST
    # =============================================================================================
    print("===== ENGLISH TEST =====")

    documents = [
        "This paper presents a machine learning approach for document classification using TF-IDF and cosine similarity.",
        "We propose an information retrieval system that ranks documents based on term frequency and inverse document frequency.",
        "Document similarity can be measured using vector space models and statistical text features.",
        "Text mining techniques are commonly used in data science and natural language processing.",
        "The football match was postponed due to heavy rain and poor weather conditions.",
        "Cooking pasta requires boiling water and adding salt before serving.",
        "TF-IDF ranking method.",
        "TF-IDF TF-IDF TF-IDF document document similarity ranking."
    ]

    query = "tf-idf document ranking"
    compute = sc(language="en")

    # ---------------- Preprocessing ----------------
    lowered_docs = timed("EN Case folding", compute.case_folding, documents)
    stemmed_docs = timed("EN Stemming", compute.stemming, lowered_docs)
    lemmatized_docs = timed("EN Lemmatization", compute.lemmatization, stemmed_docs)
    clean_docs = timed("EN Stopword removal", compute.stopword_removal, lemmatized_docs)

    lowered_query = timed("EN Query case folding", compute.case_folding, [query])[0]
    stemmed_query = timed("EN Query stemming", compute.stemming, lowered_query)
    lemmatized_query = timed("EN Query lemmatization", compute.lemmatization, stemmed_query)
    clean_query = timed("EN Query stopword removal", compute.stopword_removal, lemmatized_query)

    # ---------------- TF-IDF ----------------
    tfidf_docs = timed("EN TF-IDF training", compute.train_tfidf_weighting, clean_docs)
    tfidf_query = timed(
        "EN TF-IDF query transform",
        compute.apply_tfidf_weighting,
        [clean_query]
    )

    # ---------------- Top Words ----------------
    timed(
        "EN Top words (mean)",
        compute.set_vectorizer_vocabulary,
        tfidf_docs,
        "mean",
        10
    )

    print("\nTop EN Words (TF-IDF Mean):")
    for word, score in compute.top_word:
        print(f"{word:20s} {score:.6f}")

    # ---------------- Similarity ----------------
    similarities = timed(
        "EN Cosine similarity",
        compute.calculate_similarity,
        tfidf_query,
        tfidf_docs
    )

    print("\nEN Similarity Scores:")
    for i, score in enumerate(similarities):
        print(f"Document {i+1}: {score:.6f}")

    print("=" * 80)

    # =============================================================================================
    # INDONESIAN TEST
    # =============================================================================================
    print("===== INDONESIAN TEST =====")

    documents = [
        "Penelitian ini membahas sistem pencarian dokumen menggunakan metode TF-IDF.",
        "Makalah ini menjelaskan perhitungan bobot kata untuk peringkat dokumen.",
        "Sistem temu kembali informasi menggunakan kemiripan kosinus.",
    ]

    query = "tf-idf pencarian dokumen"
    compute = sc(language="id")

    # ---------------- Preprocessing ----------------
    lowered_docs = timed("ID Case folding", compute.case_folding, documents)
    stemmed_docs = timed("ID Stemming", compute.stemming, lowered_docs)
    lemmatized_docs = timed("ID Lemmatization", compute.lemmatization, stemmed_docs)
    clean_docs = timed("ID Stopword removal", compute.stopword_removal, lemmatized_docs)

    lowered_query = timed("ID Query case folding", compute.case_folding, [query])[0]
    stemmed_query = timed("ID Query stemming", compute.stemming, lowered_query)
    lemmatized_query = timed("ID Query lemmatization", compute.lemmatization, stemmed_query)
    clean_query = timed("ID Query stopword removal", compute.stopword_removal, lemmatized_query)

    # ---------------- TF-IDF ----------------
    tfidf_docs = timed("ID TF-IDF training", compute.train_tfidf_weighting, clean_docs)
    tfidf_query = timed(
        "ID TF-IDF query transform",
        compute.apply_tfidf_weighting,
        [clean_query]
    )

    # ---------------- Top Words ----------------
    timed(
        "ID Top words (sum)",
        compute.set_vectorizer_vocabulary,
        tfidf_docs,
        "sum",
        10
    )

    print("\nTop ID Words (TF-IDF Sum):")
    for word, score in compute.top_word:
        print(f"{word:20s} {score:.6f}")

    # ---------------- Similarity ----------------
    similarities = timed(
        "ID Cosine similarity",
        compute.calculate_similarity,
        tfidf_query,
        tfidf_docs
    )

    print("\nID Similarity Scores:")
    for i, score in enumerate(similarities):
        print(f"Document {i+1}: {score:.6f}")
