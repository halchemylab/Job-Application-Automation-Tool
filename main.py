import streamlit as st
from utils.file_manager import save_application_files
from utils.tracker import add_application, get_tracker_data
from utils.nlp_processor import extract_skills_and_keywords
from datetime import datetime, timedelta

# Set the title of the app
st.title("Job Application Automation Tool")

# Input fields for user
st.header("New Job Application")
company_name = st.text_input("Company Name")
job_title = st.selectbox("Job Title", ["Data Analyst", "Business Intelligence Analyst", "Data Scientist"])
job_description = st.text_area("Job Description")
date_applied = st.date_input("Date Applied", value=datetime.now().date())
follow_up_date = st.date_input("Follow-Up Date", value=(datetime.now() + timedelta(days=7)).date())

# Button to process and save the application
if st.button("Save Application"):
    if not company_name or not job_description:
        st.error("Please fill in all required fields.")
    else:
        # Extract skills and keywords from the job description
        extracted_data = extract_skills_and_keywords(job_description)
        skills = ", ".join(extracted_data["skills"])

        # Define placeholders for templates
        replacements = {
            "[COMPANY_NAME]": company_name,
            "[JOB_TITLE]": job_title,
            "[JOB_DESCRIPTION]": job_description,
            "[SKILLS]": skills
        }

        # Save files and update tracker
        try:
            application_folder = save_application_files(company_name, job_title, job_description, replacements)
            add_application(
                date_applied=str(date_applied),
                company_name=company_name,
                job_title=job_title,
                follow_up_date=str(follow_up_date),
                job_desc_url=None,
                status="Applied",
                feedback=""
            )
            st.success(f"Application saved successfully in {application_folder}")
        except Exception as e:
            st.error(f"Error saving application: {e}")

# Display the tracker
st.header("Application Tracker")
tracker_data = get_tracker_data()
st.dataframe(tracker_data)
