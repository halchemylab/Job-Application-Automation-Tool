# Job-Application-Automation-Tool


Project Summary
The job application automation tool will streamline the job application process by automating key steps such as customizing resumes and cover letters, organizing files, tracking applications, and sending follow-up reminders. It will use a simple and user-friendly interface powered by Streamlit for input and management. Twilio will be used to send SMS reminders for follow-ups.

Features
Resume and Cover Letter Customization:

Extract key skills and requirements from job descriptions using NLP.
Customize predefined resume and cover letter templates.
File Management:

Automatically create folders for each job application and store customized files.
Application Tracker:

Maintain a CSV file to log job details, follow-up dates, and feedback.
Follow-Up Reminders:

Send SMS notifications for follow-up dates via Twilio.
Streamlit Interface:

Simplified interface for inputting job descriptions, selecting templates, and managing applications.
Proposed File Structure
php
Copy code
job_application_tool/
├── app/                      # Main application code
│   ├── main.py               # Streamlit app entry point
│   ├── resume_templates/     # Directory for resume templates
│   │   ├── template1.docx
│   │   └── template2.docx
│   ├── cover_letter_templates/  # Directory for cover letter templates
│   │   ├── template1.docx
│   │   └── template2.docx
│   ├── utils/                # Helper functions
│   │   ├── file_manager.py   # File and folder management
│   │   ├── nlp_processor.py  # NLP processing for job descriptions
│   │   ├── tracker.py        # Functions to update CSV tracker
│   │   ├── notification.py   # Twilio SMS notifications
│   │   └── scheduler.py      # Follow-up scheduling
│   ├── data/                 # Data storage
│   │   ├── application_tracker.csv  # CSV file to track applications
│   └── static/               # Static assets (if any)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
Key Components
main.py:

Runs the Streamlit app.
Handles user input for job descriptions, template selection, and tracker management.
utils/file_manager.py:

Creates folders for applications.
Saves customized resume and cover letter files.
utils/nlp_processor.py:

Extracts key skills and qualifications from job descriptions.
utils/tracker.py:

Reads, writes, and updates the CSV tracker.
utils/notification.py:

Sends SMS notifications via Twilio.
utils/scheduler.py:

Handles scheduling and triggering follow-up reminders.
Templates Directory:

Stores Word templates for resumes and cover letters.
CSV Tracker:

Tracks job applications, including feedback and follow-up dates.
Dependencies (requirements.txt)
plaintext
Copy code
streamlit          # For the frontend
twilio             # For SMS notifications
pandas             # For managing the CSV tracker
python-docx        # For handling Word document templates
spacy              # For NLP processing
schedule           # For follow-up scheduling
openpyxl           # For working with Excel files (if needed)
pathlib            # For file management
os                 # For directory operations
Next Steps
Set up Twilio:

Create a Twilio account and get an API key, Account SID, and Auth Token.
Add this to a configuration file or environment variables for secure access.
Develop Core Features:

Build modules for file management, NLP processing, tracker updates, and notifications.
Develop Streamlit Interface:

Integrate all components into a cohesive UI.
Test and Iterate:

Test each feature independently and integrate them into the app.
Let me know if you'd like help creating detailed code snippets or drafting specific modules!
