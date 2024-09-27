import requests
import os

# Adzuna API credentials (better to store in environment variables)
API_ID = os.getenv('ADZUNA_API_ID', '97aab3e2')  # Replace with your Adzuna API ID
API_KEY = os.getenv('ADZUNA_API_KEY', 'ff4ea4d3eb3cc64ca2b4f7b5e3c9ea37')  # Replace with your Adzuna API Key

def get_job_listings(location="Pune", job_title="Data Scientist"):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": API_ID,
        "app_key": API_KEY,
        "results_per_page": 5,
        "what": job_title,
        "where": location,
        "content-type": "application/json",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None
