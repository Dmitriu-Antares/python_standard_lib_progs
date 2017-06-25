from smtplib import SMTP,SMTPAuthenticationError,SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mail_template import renderer,get_temp


file_='message.html'
template = get_temp(file_)
context = {
    "name":"Dima",
    "date":"01.03.10",
    "time":"00:15"
}



class Email:
    host = "smtp.gmail.com"
    port = 587
    def __init__(self,username,password,adress):
        self.username = username
        self.password = password
        self.to_whom = adress
    def sending(self):
        try:
            email_conn = SMTP(self.host,self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.username,self.password)

            msg=MIMEMultipart('alternative')
            msg['Subject'] = 'Python message!'
            msg['From'] = self.username
            htmlText = renderer(template,context)
            message = MIMEText(htmlText,'html')
            msg.attach(message)
            email_conn.sendmail(self.username,self.to_whom,msg.as_string())
            email_conn.quit()
            print("everithing is excellent!")
        except:
            print("something goes wrong")

'''
    type your email, pass , and another email here
'''
c = Email(,,)
c.sending()
