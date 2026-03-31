from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # remove punctuation
    return text

def get_missing_keywords(resume_text, job_desc):

    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    resume_words = set(resume_text.split())
    job_words = set(job_desc.split())

    resume_words = resume_words - ENGLISH_STOP_WORDS
    job_words = job_words - ENGLISH_STOP_WORDS

    missing = job_words - resume_words

    return list(missing)[:10]

def calculate_similarity(resume_text, job_desc):
    
    # Convert text to embeddings (numbers)
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_desc])
    
    # Compute similarity score
    score = cosine_similarity(resume_embedding, job_embedding)
    
    return score[0][0]

