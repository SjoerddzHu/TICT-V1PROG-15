import socket
import time
import smtplib

from threading import Timer

# --- Hier worden alle variabelen gedefineerd
s = socket.socket()
host = socket.gethostbyname('192.168.42.1')
port = 12221
s.bind((host, port))

s.listen(5)
c = None
connectionlist = []


GPIO= 1
TO= "jaco.cloete@student.hu.nl" #all of the credentials
GMAIL_USER="csnproject2017@gmail.com"
PASS= "project123"
SUBJECT = 'Alert!'
TEXT = 'Er is een inbreker gesignaleerd in uw woning!'

# Met deze functie wordt mail verstuurt vanaf onze Gmail account naar mijn email.
def send_mail(): #the texting portion
    print ("Sending text")
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(GMAIL_USER,PASS)
    header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
    print (header)
    msg = header + '\n' + TEXT + '\n\n'
    server.sendmail(GMAIL_USER,TO,msg)
    server.quit()
    time.sleep(1)
    print ("Text sent")

# Met deze functie kunnen we een pakketje versturen om het alarmsysteem op afstand aan tezetten.

def alarmSwitch():
    global c
    try:
        c.send('check'.encode('ascii'))
    except:
        print('Alarm')
        c = None
        send_mail()
    if(input() == 'switch'):
        c.send('101'.encode('ascii')) # Hier versturen wij een pakketje naar de client om het alarmsysteem aan tezetten
    else:
        print('error')

while True:
    # Als er nog geen verbinding is met het alarmsysteem
    # hier onder wacht hij op een verbinding
   if c is None:
       # Halts
       print('[Waiting for connection...]')
       c, addr = s.accept()
       connectionlist.append(c)
       print('Got connection from', addr)
       # Als hij verbinding heeft komt hij in deze gedeelte
   else:
       # Halts
       try:
           # hier wacht de server op een response van de client
           print('[Waiting for response...]')
           t= Timer(1.0, alarmSwitch) # after 30 seconds, "hello, world" will be printed
           t.start()
           bericht = c.recv(1024)

           print(bericht.decode('ascii'))
           
           # Hier wordt de response van de client afgevangen.
           if(bericht.decode('ascii') != ''):
                n = eval(bericht.decode('ascii'))
                if n == 0:
                    print('Security system is offline')
                elif n == 1:
                    print('Security system is online')
                elif n == 2:
                    print('You have 10 seconds to correctly enter the code.')
                elif n == 3:
                    print('Alarm! Send back-up!')
                    send_mail()
                else:
                    print('Delete system 32.')
            # Als hij de TRY niet kan uitvoeren zet hij de client weer op none!
       except:
            c = None
            print('Alarm')
            send_mail()   
