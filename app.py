import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.scorer import calculate_similarity, get_missing_keywords

st.title("AI Career Assistant 🚀")

# Upload resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# Job description input
job_desc = st.text_area("Paste Job Description")

st.info("👆 Upload resume and paste job description, then click below to analyze!")

if st.button("Analyze My Fit") and uploaded_file and job_desc:

    
    # Extract resume text
    resume_text = extract_text_from_pdf(uploaded_file)
    
    # Calculate similarity
    score = calculate_similarity(resume_text, job_desc)
    
    # Get missing keywords
    missing = get_missing_keywords(resume_text, job_desc)
    
    st.subheader("Results")
    
    st.write(f"Match Score: {round(score * 100, 2)}%")
    
    st.write("Missing Skills:")
    st.write(missing)