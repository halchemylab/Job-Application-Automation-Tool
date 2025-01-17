import spacy
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Cleans and preprocesses job description text by removing special characters and extra whitespace.
    
    :param text: Raw job description text
    :return: Cleaned text
    """
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # Normalize whitespace
    return text.lower()

def extract_skills_and_keywords(job_description):
    """
    Extracts key skills and keywords from a job description.

    :param job_description: The raw job description text
    :return: A dictionary containing extracted skills and keywords
    """
    # Preprocess the text
    cleaned_description = clean_text(job_description)

    # Tokenize and analyze text with SpaCy
    doc = nlp(cleaned_description)

    # Extract nouns and proper nouns (common in job descriptions for skills)
    nouns = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"] and token.text not in ENGLISH_STOP_WORDS]

    # Extract verbs (useful for action-oriented language like "analyze", "optimize")
    verbs = [token.text for token in doc if token.pos_ == "VERB" and token.text not in ENGLISH_STOP_WORDS]

    # Combine nouns and verbs and count frequency
    all_keywords = nouns + verbs
    keyword_counts = Counter(all_keywords)

    # Filter out low-frequency keywords (e.g., less than 2 mentions)
    filtered_keywords = {word: count for word, count in keyword_counts.items() if count > 1}

    # Identify skill-related keywords (heuristic-based for now)
    potential_skills = [word for word in filtered_keywords if len(word) > 3]

    return {
        "skills": potential_skills,
        "keywords": list(filtered_keywords.keys())
    }

# Example usage
if __name__ == "__main__":
    job_description = """
    We are looking for a Data Scientist with experience in Python, machine learning, and big data tools like Spark.
    Responsibilities include analyzing datasets, building predictive models, and optimizing data pipelines.
    Familiarity with cloud platforms such as AWS or GCP is a plus.
    """

    result = extract_skills_and_keywords(job_description)
    print("Extracted Skills:", result["skills"])
    print("Extracted Keywords:", result["keywords"])
