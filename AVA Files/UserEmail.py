import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


RECEPIENT = 'testpersonnumberone@gmail.com'
content = ''

#Sending Emails with Subject
def SendSubEmail(to, subject, text):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    message = content
    
    #MIMEMultiplayer for adding in 'Subject' aswell
    msg = MIMEMultipart()
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach((MIMEText(message,'plain')))

    #Senders email(Login Credentials)
    server.login('testpersonnumberone@gmail.com', 'Testperson1!')

    text = msg.as_string()
    server.sendmail(RECEPIENT, to, text)
    
    #Important to close the server after sending
    server.close()