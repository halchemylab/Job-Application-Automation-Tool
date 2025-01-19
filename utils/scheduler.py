import schedule
import time
from datetime import datetime
from utils.notification import send_sms_notification
from utils.tracker import get_tracker_data

# Constants
NOTIFICATION_PHONE_NUMBER = "+17816986521"  # Replace with your phone number


def send_follow_up_reminders():
    """
    Check the application tracker for follow-up dates and send reminders if needed.
    """
    try:
        # Load tracker data
        tracker_data = get_tracker_data()

        # Current date
        today = datetime.now().date()

        # Iterate through the tracker
        for _, row in tracker_data.iterrows():
            follow_up_date = datetime.strptime(row["Follow-Up Date"], "%Y-%m-%d").date()

            # Check if today matches the follow-up date
            if follow_up_date == today:
                company_name = row["Company Name"]
                job_title = row["Job Title"]
                message = (
                    f"Reminder: Follow up with {company_name} for {job_title} position applied on {row['Date Applied']}!"
                )

                # Send the SMS
                send_sms_notification(NOTIFICATION_PHONE_NUMBER, message)
                print(f"Reminder sent for {company_name} - {job_title}")

    except Exception as e:
        print(f"Error in sending reminders: {e}")


def schedule_reminders():
    """
    Schedule the follow-up reminders to run daily.
    """
    schedule.every().day.at("09:00").do(send_follow_up_reminders)  # Set time to 9:00 AM

    print("Scheduler is running. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait before checking again

# Example usage
if __name__ == "__main__":
    schedule_reminders()