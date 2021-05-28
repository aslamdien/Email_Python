import smtplib
# please note go to https//myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates STMP session

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_1d = 'aslamdien90@gmail.com'
receiver_email_id = 'aslamdien90@gmail.com'
password = input("Enter senders email password: ")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_1d, password)

message = "HI guys how are you. I am doing fine\n"
message = message + " How was your task yesterday"

s.sendmail(sender_email_1d, receiver_email_id, message)

s.quit()
