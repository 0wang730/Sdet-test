import smtplib
import ssl
from email.message import EmailMessage


class Email(object):

    def send_email(self, message):
        # Use the smtplib module to send plain text emails

        EMAIL_ADDRESS = ""  # Your Email address
        EMAIL_PASSWORD = ""  # Your Authorization code

        # Use ssl module's context to load system-approved certificates for verification at login
        context = ssl.create_default_context()
        # Create a list to store the target email addresses
        contacts = ['']
        # To prevent forgetting to close the connection, you can also use a with statement
        with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context) as smtp:  # Complete encrypted communication
            # After successfully connecting, use the login method to log into your email
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for contact in contacts:
                subject = "test_report"
                body = f"{contact}\n{message}"
                msg = EmailMessage()
                msg['subject'] = subject  # Email subject
                msg['From'] = EMAIL_ADDRESS  # Email sender
                msg['To'] = contact  # Email recipient
                msg.set_content(body)  # Set the body content of the email using set_content() method
                # Use send_message method to send the email information
                smtp.send_message(msg)
