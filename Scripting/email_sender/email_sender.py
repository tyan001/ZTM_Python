import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASS")

if not email_user or not email_password:
    raise ValueError("Missing EMAIL_USER or EMAIL_PASS in .env file")

msg = EmailMessage()
msg.set_content("This is a test email sent from Python.")
msg["Subject"] = "Python Test"
msg["From"] = email_user
msg["To"] = "recipient@example.com"

# For Gmail/Outlook (Port 587 with TLS)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email_user, email_password)
    server.send_message(msg)
