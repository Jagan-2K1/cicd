
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



#
# name: CHECKING SERVER STATUS
# on:
#   push:
#     branches:
#       - jagannath
#
# concurrency:
#   group: jagannath
#   cancel-in-progress: true
#
# jobs:
#   deploy:
#     name: Continuous Integration
#     uses: ./.github/workflows/master.yml
#     with:
#       SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
#       SSH_HOST: ${{ secrets.SSH_HOST }}
#       SSH_USER: ${{ secrets.SSH_USER }}
#
#   mail-service:
#     name: Mail Sending
#     needs: deploy
#     runs-on: ubuntu-latest
#     steps:
#       - name: Configure SSH
#         env:
#           SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
#           SSH_HOST: ${{ secrets.SSH_HOST }}
#           SSH_USER: ${{ secrets.SSH_USER }}
#         run: |
#           mkdir -p ~/.ssh/
#           echo "$SSH_PRIVATE_KEY" > ~/.ssh/github
#           chmod 600 ~/.ssh/github
#           cat >> ~/.ssh/config <<END
#           Host target
#             HostName $SSH_HOST
#             User $SSH_USER
#             IdentityFile ~/.ssh/github
#             LogLevel ERROR
#             StrictHostKeyChecking no
#           END
#
#       - name: Checking server Status
#         run: |
#           ps aux | grep 'python manage.py runserver 0.0.0.0:2914' | grep -v grep
#         id: check_server_status
#
#       - name: Print server status
#         run: echo "${{ steps.check_server_status.outputs }}"
#

