# skipped your comments for readability
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "rndjsports@gmail.com"
my_password = r"rndjsports123"


def mail(decision,applicants):
    
    you = "amoghd9@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alert"
    msg['From'] = me
    msg['To'] = you

    html1 = '<html><body><p>Hello,</p><p> We are sorry to inform you that you have not been selected as a volunteer for The Apprentice Project.<br />You have not been shortlisted.</p><p>Thanking You,<br />The Apprentice Project.</p></body></html>'
    html2 = '<html><body><p>Hello,</p><p> Congratulations!! Welcome to the team. <br />We are overjoyed to inform you that you have made the cut.<br />We shall send you a follow-up mail providing you with all the details.</p><p>Thanking You,<br />The Apprentice Project</p></body><html>'
    if decision is '1':
        html = html2
    else:
        html = html1

    part2 = MIMEText(html, 'html')

    msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

mail(1,aplicants_1)
mail(0,aplicants_0)