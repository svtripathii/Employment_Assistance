import streamlit as st
from job_fetcher import get_job_listings
import os

# Create two columns: one for the image and one for the title
col1, col2 = st.columns([1, 4])  # Adjust the width ratio as necessary

with col1:
    # Display the logo in the first column (left)
    st.image("logo.png", width=100)  # Adjust the width if necessary

with col2:
    # Display the title in the second column (right)
    st.title("Employment Assistance - Locate Job Opportunities")

# Search Criteria Section
st.subheader("Search Criteria")
location = st.text_input("Enter Job Location")
selected_job_type = st.text_input("Enter Job Title")

# Job Listings Section
if st.button("Search Jobs"):
    if location and selected_job_type:
        jobs_data = get_job_listings(location, selected_job_type)  # Fetch the job listings
        
        if jobs_data and 'results' in jobs_data:
            job_listings = jobs_data['results']
            st.subheader(f"Live Job Listings for '{selected_job_type}' in '{location}':")
            
            for job in job_listings:
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; border-radius: 8px; padding: 10px; margin: 10px;">
                        <h4>{job.get('title', 'N/A')}</h4>
                        <p><strong>Location:</strong> {job.get('location', {}).get('display_name', 'N/A')}</p>
                        <p><strong>Company:</strong> {job.get('company', {}).get('display_name', 'N/A')}</p>
                        <p>{job.get('description', 'No description available')[:200]}...</p>
                        <a href="{job.get('redirect_url', '#')}" target="_blank">Apply Here</a>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        else:
            st.write("No job listings found. Try a different location or job title.")
    else:
        st.write("Please enter both location and job title.")
