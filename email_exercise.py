# Exercise Email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Structur Of Email
sender_email_id = 'aslamdien90@gmail.com' # Senders Address
receiver_email_id = ['thapelo@lifechoices.co.za', 'sithandathuzipho@gmail.com', 'alamdien90@gmail.com']# Receivers Address
password = input("Enter Your Password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ', ' .join(receiver_email_id)
msg['Subject'] = subject
body = "HI guys how are you. I am doing fine\n"
body = body + "How was yor task yesterday"
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# Start TLS for security
s.starttls()
 #Authentication
s.login(sender_email_id, password)
# message to be saved

# sending the mall
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the season
s.quit()
