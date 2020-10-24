import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


RECEPIENT = 'testpersonnumberone@gmail.com'
content = ''

#Sending Emails with Subject
def SendSubEmail(to, subject, text):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        message = content
        
        #MIMEMultiplayer for adding in 'Subject' aswell
        msg = MIMEMultipart()
        msg['To'] = to
        msg['Subject'] = subject

        part1 = MIMEText(text, "plain")

        msg.attach(part1)

        #Senders email(Login Credentials)
        server.login('testpersonnumberone@gmail.com', 'Testperson1!')

        text = msg.as_string()
        server.sendmail(RECEPIENT, to, text)
    
    except Exception as e:
        print("Something Went Wrong")
    #Important to close the server after sending
    finally:
        server.close()