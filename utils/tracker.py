import os
import pandas as pd
from pathlib import Path

# Path to the application tracker CSV
TRACKER_FILE = Path("data/application_tracker.csv")

# Ensure the directory exists
TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)

# Define the tracker columns
TRACKER_COLUMNS = [
    "Date Applied",
    "Company Name",
    "Job Title",
    "Follow-Up Date",
    "Job Description URL",
    "Status",
    "Feedback"
]

def initialize_tracker():
    """
    Initializes the tracker file if it doesn't already exist.
    """
    if not TRACKER_FILE.exists():
        df = pd.DataFrame(columns=TRACKER_COLUMNS)
        df.to_csv(TRACKER_FILE, index=False)

def add_application(date_applied, company_name, job_title, follow_up_date, job_desc_url=None, status="Applied", feedback=""):
    """
    Adds a new application entry to the tracker.

    :param date_applied: Date of application (YYYY-MM-DD)
    :param company_name: The name of the company
    :param job_title: The job title
    :param follow_up_date: Date for follow-up (YYYY-MM-DD)
    :param job_desc_url: URL to the job description (optional)
    :param status: Status of the application (default: "Applied")
    :param feedback: Notes or feedback for the application (default: empty string)
    """
    # Load the tracker
    df = pd.read_csv(TRACKER_FILE)

    # Create a new entry
    new_entry = {
        "Date Applied": date_applied,
        "Company Name": company_name,
        "Job Title": job_title,
        "Follow-Up Date": follow_up_date,
        "Job Description URL": job_desc_url,
        "Status": status,
        "Feedback": feedback
    }

    # Append the entry and save
    df = df.append(new_entry, ignore_index=True)
    df.to_csv(TRACKER_FILE, index=False)

def update_application(company_name, job_title, updates):
    """
    Updates an existing application entry in the tracker.

    :param company_name: The name of the company
    :param job_title: The job title
    :param updates: A dictionary of column names and their new values
    """
    # Load the tracker
    df = pd.read_csv(TRACKER_FILE)

    # Find the matching row
    mask = (df["Company Name"] == company_name) & (df["Job Title"] == job_title)

    if not mask.any():
        raise ValueError(f"No application found for {company_name} - {job_title}.")

    # Update the specified columns
    for column, value in updates.items():
        if column in df.columns:
            df.loc[mask, column] = value

    # Save the updated tracker
    df.to_csv(TRACKER_FILE, index=False)

def get_tracker_data():
    """
    Loads and returns the tracker data as a Pandas DataFrame.

    :return: Pandas DataFrame containing tracker data
    """
    return pd.read_csv(TRACKER_FILE)

# Initialize the tracker when the script is loaded
initialize_tracker()

# Example usage
if __name__ == "__main__":
    # Add a new application
    add_application(
        date_applied="2025-01-16",
        company_name="Awesome Tech",
        job_title="Data Scientist",
        follow_up_date="2025-01-23",
        job_desc_url="https://example.com/job/data-scientist"
    )

    # Update the application
    update_application(
        company_name="Awesome Tech",
        job_title="Data Scientist",
        updates={"Status": "Interview Scheduled", "Feedback": "Interview on 2025-01-20."}
    )

    # Print tracker data
    print(get_tracker_data())
