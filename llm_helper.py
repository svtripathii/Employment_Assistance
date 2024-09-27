from transformers import pipeline
import os

# Hugging Face API Key (store in environment variables for security)
API_KEY = os.getenv('HUGGINGFACE_API_KEY', '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')  # Replace with your Hugging Face API key

def get_job_recommendations(job_title):
    # Initialize the LLM model using the Hugging Face pipeline
    llm = pipeline("text-generation", model="gpt2", config={"use_auth_token": API_KEY})

    # Generate job recommendations based on job title
    recommendations = llm(f"Suggest job roles for a {job_title}:", max_length=50)

    return [rec['generated_text'] for rec in recommendations]
