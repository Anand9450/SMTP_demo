import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'

# Email content
receiver_email = 'recipient_email@example.com'
subject = 'Test Email from Python'
body = 'This is a test email sent using Python and SMTP.'

# Create a MIME object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    print('Email sent successfully!')

except Exception as e:
    print(f'Failed to send email. Error: {str(e)}')

finally:
    # Terminate the SMTP session and close the connection
    server.quit()
