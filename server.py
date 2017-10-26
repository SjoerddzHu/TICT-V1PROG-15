import socket

from threading import Timer


s = socket.socket()
host = socket.gethostname()
port = 12221
s.bind((host, port))

s.listen(5)
c = None
connectionlist = []

import time
import smtplib
GPIO= 1
TO= "jaco.cloete@student.hu.nl" #all of the credentials
GMAIL_USER="csnproject2017@gmail.com"
PASS= "project123"
SUBJECT = 'Alert!'
TEXT = 'Er is een inbreker gesignaleerd in uw woning!'

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
     
def alarmSwitch():
    global c
    if(input() == 'switch'):
        c.send('101'.encode('ascii'))
    else:
        print('error')

while True:
   if c is None:
       # Halts
       print('[Waiting for connection...]')
       c, addr = s.accept()
       connectionlist.append(c)
       print('Got connection from', addr)
   else:
       # Halts
       try:
           print('[Waiting for response...]')
           t= Timer(1.0, alarmSwitch) # after 30 seconds, "hello, world" will be printed
           t.start()
           bericht = c.recv(1024)

           print(bericht.decode('ascii'))
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
       except:
            c = None