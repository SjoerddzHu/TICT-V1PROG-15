import socket
import RPi.GPIO as GPIO
from threading import Timer
import os
import time

GPIO.setwarnings(False)
  
OraLedPin = 13       # Pin13 --- Orange led
OraBtnPin = 16       # Pin16 --- Orange button
RedLedPin = 11
RedBtnPin = 12
GrnLedPin = 15
GrnBtnPin = 18
Buzzer = 19

GrnLed_status = 1    # Status 0 = ON status 1 = OFF
OraLed_status = 1
RedLed_status = 1

s = ""               # Hier komt de socket

def connection():    # Connectie maken met de server
    global s
    connection = False    # Er is geen conecctie
    while connection == False :     # Als er geen connectie is probeert hij hem te maken
        try:
            s = socket.socket()      # s word de socket
            host = socket.gethostbyname('145.89.100.170')   #IP van server
            port = 12221     # Portnummer
            s.connect((host, port))        # Connect
            print('Connected to', host)   # Bevestiging dat hij verbonden is
            connection = True          # Connectie waarde word veranderd
        except:    # Als er geen verbinding gemaakt kan worden of hij valt weg
            print('Alarm')  #ALARM 
            global RedLed_status # Rode lamp gaat aan
            RedLed_status = 0
            GPIO.output(RedLedPin,RedLed_status)
            time.sleep(1)    #hij hoeft maar 1 keer per seconde te kijken of hij kan verbinden

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
            
    GPIO.setup(RedLedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(RedBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(RedLedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
            
    GPIO.setup(OraLedPin, GPIO.OUT)
    GPIO.setup(OraBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(OraLedPin, GPIO.HIGH)
            
    GPIO.setup(GrnLedPin, GPIO.OUT) 
    GPIO.setup(GrnBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(GrnLedPin, GPIO.HIGH)
    global GrnLed_status    # Variabelen worden opnieuw geinitialiseerd
    global OraLed_status
    global RedLed_status
    global t
    global BuzzerPin
    global Buzzer
    GrnLed_status = 1
    OraLed_status = 1
    RedLed_status = 1

    BuzzerPin = Buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    t = Timer(10.0,Alarm)   # De 10 seconde timer word aangemaakt

def GrnswLed(ev=None):      # Waneer de groene knop word ingedrukt
    global GrnLed_status
    GrnLed_status = not GrnLed_status
    GPIO.output(GrnLedPin, GrnLed_status)  # Switch led status(on-->off; off-->on)
    if GrnLed_status == 1:   # Als groen uitgaat zegt hij Alarm OFF en dit verstuurd hij naar de server
        print ('Alarm OFF')
        sendPacket('0')
    else:     # Als groen aangaat zegt hij Alarm ON en dit word verstuurd naar de server
        print ('Alarm ON')
        sendPacket('1')
        
def RedswLed(ev=None):      # Als de rode knop ingedrukt word
    global GrnLed_status
    global RedLed_status
    global OraLed_status
    if GrnLed_status == 0 and RedLed_status == 1:    # Als het groene lampje aan staat en het rode lampje uit
        OraLed_status = not OraLed_status        # Variabele word omgedraaid
        GPIO.output(OraLedPin, OraLed_status)  # Switch led status(on-->off; off-->on)
        if OraLed_status == 0:          # Als het oranje lampje aan staat
            print ('Voer code in:')    # Vragen om de code
            sendPacket('2')        # Verteld de server dat er iemand binnen is
            global t
            t.start()     # Hij start de tijd waarin je de code in moet voeren

def OraswLed(ev=None):     # Als de orange knop word ingedrukt
    print ("code goed")     # Print dat de code goed is ingevoerd
    sendPacket('0')       # Verstuur deze info naar de server
    GPIO.output(BuzzerPin, GPIO.HIGH)
    setup()         # Reset alles naar de beginstand

def loop():
    GPIO.add_event_detect(GrnBtnPin, GPIO.FALLING, callback=GrnswLed, bouncetime=200) # Als de groene knop in word ingedrukt etc.
    GPIO.add_event_detect(RedBtnPin, GPIO.FALLING, callback=RedswLed, bouncetime=200) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
    GPIO.add_event_detect(OraBtnPin, GPIO.FALLING, callback=OraswLed, bouncetime=200)
    while True:
        global s
        b = s.recv(1024)         # Ontvang pakketen van de server
        if b.decode('ascii') == '101':     # Decoodeer het bericht 
            GrnswLed()       # Zet het alarm aan/uit
        time.sleep(1)   # Wachten op volgende bericht
		
def sendPacket(value):    #Waneer er een packet verstuurd moet worden
    try:
        global s
        s.send(value.encode('ascii'))     # Hij codeert het bericht en verstuurt het naar de server
    except :
        print('alarm')          # Op het moment dat er geen verbinding is runt hij opnieuw connection() om verbinding te zoeken anders gaat het alarm af
        connection()

def Alarm():         # Wanneer de timer voor het invoeren van de code over is
    global OraLed_status
    global RedLed_status
    if OraLed_status == 0:     # Als het orange lampje aan is 
        print ('inbreker')      
        OraLed_status = not OraLed_status
        GPIO.output(OraLedPin, OraLed_status) # Het orange lampje gaat uit
        RedLed_status = not RedLed_status
        GPIO.output(RedLedPin,RedLed_status) # Het rode lampje gaat aan
        sendPacket('3')       # Er word naar de server verstuurd dat er een inbreker is
        while OraLed_status == 1 and RedLed_status == 0:
            GPIO.output(BuzzerPin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(BuzzerPin, GPIO.HIGH)
            time.sleep(0.1)
        

def destroy():
    GPIO.output(RedLedPin, GPIO.HIGH)     # Alle leds gaan uit
    GPIO.output(OraLedPin, GPIO.HIGH)
    GPIO.output(GrnLedPin, GPIO.HIGH)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Programma begint hier
    setup()      # Eerst loopt hij door de setup en de connection
    connection()
    try:
        loop()     # Dan blijft loop() runnen 
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()