
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender_email = 'jagannath@vivyacorp.com'
receiver_email = 'pooja@vivyacorp.com'
password = 'J@8667832235'

# Email content
subject = 'Alert Server Down'
body = 'After the CICD Merge Vivya Chatbot server is DOWN !.'

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, 'plain'))

try:
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Use your SMTP server and port
    session.starttls()  # Enable security
    session.login(sender_email, password)  # Login with email ID and password
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent Successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
