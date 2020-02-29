# Coded By Afrizal F.A
# Rework By Rahman Gunawan
import sys, asyncio, smtplib, random, string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("""
 _  _       _ _           
|  \ | _ _() | _ _ __ 
| |\ |/ _` | | |/ _ \__|
| |  | | (_| | | |  __/ |   
|_|  |_|\,_|_|_|\_|_|   
                            
""")
def Subject(): #Multi-Subject
    subject_line = 0
    subject_list = open('Subject.txt', 'r')
    count_subject = len(open('Subject.txt').readlines())
    with subject_list as subject:
        subject_split = [line.rstrip() for line in subject]
    #Subject Split
    if (subject_line == count_subject):
        subject_line = 0
    subject = subject_split[subject_line]
    subject_line+=1
    subject_replaced = subject.replace("##code##", fakecase())
    subject_replaced = subject_replaced.replace(" ","%20")
    subject_replaced = subject_replaced.replace("%20", " ")
    subject_replaced = subject_replaced.replace("%23", "#")
    return subject_replaced

def fakecase():
    while True:
        #Generate Random Case number
        randchar0 =random.choice(string.ascii_uppercase)
        randchar1 =random.choice(string.ascii_uppercase)
        randchar2 =random.choice(string.ascii_uppercase)
        randchar3 =random.choice(string.ascii_uppercase)
        randchar4 =random.choice(string.ascii_uppercase)
        randint0 = random.randrange(0,9)
        randint1 = random.randrange(0,9)
        randint2 = random.randrange(0,9)
        randint3 = random.randrange(0,9)
        randint4 = random.randrange(0,9)
        code = "%23"+randchar0+randchar1+randchar2+str(randint0)+str(randint1)+randchar3+str(randint2)+str(randint3)+str(randint4)+randchar4
        return code

async def kirim_email(sender, target):
    try :
        mail.sendmail(sender, target, pesan.as_string())
        print("[*] Sending To : " + target)
    except :
        print("[*] Failed Send To : " + target)

host = "email-smtp.us-west-2.amazonaws.com"
port = int(587)
user = "AKIA2IJANXFFO6A7Z2GA"
password = "BOeoCphZ3f5g9Rv3EBB3evlVqRF7/BWQG82Og4xTulOl"
sender_mail ="noreply@gatjed.com"
html_file = "letteramazon.html"
file_list = "list.txt"

mail = smtplib.SMTP(host, port)
mail.ehlo()
mail.starttls()
mail.login(user, password)

html = open(html_file, "r").read()
html = MIMEText(html, 'html')

pecah_mail_list = open(file_list, "r").read().split('\n')
for target in pecah_mail_list :
    if not target :
        continue
    
    pesan = MIMEMultipart('alternative')
    pesan['Subject'] = Subject()
    pesan['From'] = "Amazon <noreply@gatjed.com>"
    pesan['To'] = target
    pesan.attach(html)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(kirim_email(sender_mail, target))
    
mail.quit()