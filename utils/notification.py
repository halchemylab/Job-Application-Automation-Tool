from twilio.rest import Client
import os

# Twilio configuration (use environment variables for security)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Ensure all required environment variables are set
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
    raise EnvironmentError("Twilio environment variables not properly configured.")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_notification(to_phone_number, message):
    """
    Sends an SMS notification using Twilio.

    :param to_phone_number: Recipient's phone number (E.164 format, e.g., "+1234567890")
    :param message: The message to send
    """
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"Message sent successfully. SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Failed to send message: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example data
    recipient_phone = "+17816986521"  # Replace with a valid phone number
    reminder_message = "Reminder: Follow up with Awesome Company for Data Scientist position applied on 2025-01-16."

    # Send the SMS
    send_sms_notification(recipient_phone, reminder_message)
