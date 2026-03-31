from transformers import pipeline

# Load model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_feedback(resume_text, job_desc, missing_skills):

    prompt = f"""
    You are an expert career coach.

    Analyze the resume and job description.

    Missing skills: {missing_skills}

    Give clear and practical suggestions to improve the resume.
    Be specific and short.
    """

    result = generator(prompt, max_length=200, do_sample=True)

    return result[0]['generated_text']
