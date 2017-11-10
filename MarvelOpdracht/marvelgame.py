import io
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen
import datetime
import time
import hashlib
import random
import json
from pprint import pprint
import urllib.parse
import urllib.request
import pygame
import tkinter as tk
public_key= '4064284226f9e256089157d38a1a1958'
private_key= '17d325bb6bf9e0b9e67e6685276ba8ccd295e5b5'

characterAPI = 'http://gateway.marvel.com/v1/public/characters?%s'

root = Tk()
root.title("super wonder captain")
root.configure(background="#ed1a23")
root.geometry("750x470")
root.resizable(width=False, height=False)


def countdown(count):
    # veranderd text in Count_icon
    Count_icon['text'] = count
    if count > 0:  #Als het aantal secondes groter is dan 0 seconde
        root.after(1000, countdown, count-1) #snelheid 1 seconde
    if count == 90: #Als het aantal secondes 90 is
        pygame.mixer.init() # Speelt het geluid 'time.wav' af
        pygame.mixer.music.load("time.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif count == 0:  #Als het aantal secondes 0 is
        print("Game Over")
        pygame.mixer.init()# Speelt het geluid 'gameover.wav' af
        pygame.mixer.music.load("gameover.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue


Count_icon = Label(root, bg="#ed1a23", font=("Calibri", 16)) #De background kleur "#edla23 en het lettertype
countdown(320)  # Aantal secondes voor de countdown


def apiHandeler_Json(APIurl):
    st = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")

    paramameter = {}
    paramameter['ts'] = str(time.time())
    paramameter['apikey'] = public_key
    privateKey = private_key
    paramameter['hash'] = hashlib.md5(bytes(paramameter['ts'] + privateKey + paramameter['apikey'], 'utf-8')).hexdigest()
    # q['name'] = 'Spider-Man'

    if 'characters' in APIurl:
        paramameter['offset'] = random.randrange(1492)
        paramameter['limit'] = 1

    params = urllib.parse.urlencode(paramameter)
    url = APIurl % params
    with urllib.request.urlopen(url) as f:
        data = json.load(f)
    return data

def GetHero():
    print('getHero functie')
    check = False

    while check == False:
        data = apiHandeler_Json(characterAPI)
        results = data['data']['results']
        global name
        name = results[0]['name']
        global description
        description = results[0]['description']
        thumbnailURL = results[0]['thumbnail']['path']
        global imgUrl
        imgUrl = thumbnailURL + '/portrait_xlarge.jpg'
        characterItemsLen = len(data['data']['results'][0]['events']['items'])
        global characterItems
        characterItems = []
        try:
            characterItems = data['data']['results'][0]['events']['items'][random.randrange(characterItemsLen)]['name']
        except ValueError:
            characterItemsLen = 0
        print(name, description, imgUrl,'and appears in: ', characterItems)
        if 'image_not_available' not in imgUrl and description != '' and name != '' and characterItems != []:
            check = True

def GiveUp():
     Button_GiveUp.config(state=DISABLED)
     Current_Points = eval(Points.get(1.8, END))
     New_Points = Current_Points - 8
     Points.config(state=NORMAL)
     Points.delete(1.8, END)
     Points.insert(1.8, New_Points)
     Points.config(state=DISABLED)
     global imgUrl
     pic_url = imgUrl
     my_page = urlopen(pic_url)
     my_picture = io.BytesIO(my_page.read())
     pil_img = Image.open(my_picture)
     tk_img = ImageTk.PhotoImage(pil_img)
     label = Label(root, image=tk_img, bg="#ed1a23")
     label.grid(row=0, column=0)
     global name
     print("kom ik hier")
     Hero.insert(END,name)
     geefhint1()
     geefhint2()
     geefhint3()
     geefhint4()
     geefhint5()


def NextHero():
    GetHero()
    Button_Submit.config()
    Button_Next.config()
    Photo = PhotoImage(file="Questionmark.png")
    Picture = Label(root, bg="#ed1a23", image=Photo)
    Picture.place(x=0, y=0)
    Button_Submit.config(state=NORMAL)
    Button_Next.config(state=DISABLED)
    Hero.delete(0, END)
    resetHints()
    root.mainloop()


def resetHints():
    Button_GiveUp.config(state=NORMAL)
    output.config(state=NORMAL)
    output2.config(state=NORMAL)
    output3.config(state=NORMAL)
    output4.config(state=NORMAL)
    output.delete(1.0,END)
    output2.delete(1.0,END)
    output3.delete(1.0,END)
    output4.delete(1.0,END)
    Button_GiveUp.config(state=DISABLED)
    output.config(state=DISABLED)
    output2.config(state=DISABLED)
    output3.config(state=DISABLED)
    output4.config(state=DISABLED)
    Button_GiveUp.config(state=NORMAL)
    Hint1button.config(state=NORMAL)
    Hint2button.config(state=NORMAL)
    Hint3button.config(state=NORMAL)
    Hint4button.config(state=NORMAL)
    Hint5button.config(state=NORMAL)



def Submit():
    Input_Name = Hero.get()
    global name
    if name.lower() == Input_Name.lower():
        print("You win")
        pygame.mixer.init()
        pygame.mixer.music.load("Sound.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        global imgUrl
        pic_url = imgUrl
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label = Label(root, image=tk_img, bg="#ed1a23")
        label.grid(row=0, column=0)
        Current_Points = eval(Points.get(1.8, END))
        New_Points = Current_Points + 25
        Points.config(state=NORMAL)
        Points.delete(1.8, END)
        Points.insert(1.8, New_Points)
        Points.config(state=DISABLED)
        Button_Submit.config(state=DISABLED)
        Button_Next.config(state=NORMAL)

        root.mainloop()

    else:
        pygame.mixer.init()
        pygame.mixer.music.load("Wrong.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        Current_Points = eval(Points.get(1.8, END))
        New_Points = Current_Points - 1
        Points.config(state=NORMAL)
        Points.delete(1.8, END)
        Points.insert(1.8, New_Points)
        Points.config(state=DISABLED)

def geefhint1():
    output.config(state=NORMAL)
    global name
    output.insert(END,"first three letters of the name: " + name[0:3] )                                  #print de hint
    output.config(state=DISABLED)
    Hint1button.config(state=DISABLED)
    Current_Points = eval(Points.get(1.8, END))
    New_Points = Current_Points - 3
    Points.config(state=NORMAL)
    Points.delete(1.8, END)
    Points.insert(1.8, New_Points)
    Points.config(state=DISABLED)

def geefhint2():
    output2.config(state=NORMAL)
    global description
    output2.insert(END, "Character Bio: " + description )                           #print de hint
    output2.config(state=DISABLED)
    Hint2button.config(state=DISABLED)
    Current_Points = eval(Points.get(1.8, END))
    New_Points = Current_Points - 3
    Points.config(state=NORMAL)
    Points.delete(1.8, END)
    Points.insert(1.8, New_Points)
    Points.config(state=DISABLED)


def geefhint3():
    global characterItems
    output3.config(state=NORMAL)
    output3.insert(END, "Appears in the follwing major event: " + characterItems)                            #print de hint
    output3.config(state=DISABLED)
    Hint3button.config(state=DISABLED)
    Current_Points = eval(Points.get(1.8, END))
    New_Points = Current_Points - 3
    Points.config(state=NORMAL)
    Points.delete(1.8, END)
    Points.insert(1.8, New_Points)
    Points.config(state=DISABLED)

def geefhint4():
    output4.config(state=NORMAL)
    global name
    output4.insert(END, "The name contains {} Characters.".format(len(name)))                           #print de hint
    output4.config(state=DISABLED)
    Hint4button.config(state=DISABLED)
    Current_Points = eval(Points.get(1.8, END))
    New_Points = Current_Points - 3
    Points.config(state=NORMAL)
    Points.delete(1.8, END)
    Points.insert(1.8, New_Points)
    Points.config(state=DISABLED)


def geefhint5():
    Hint5button.config(state=DISABLED)
    Current_Points = eval(Points.get(1.8, END))
    New_Points = Current_Points - 5
    Points.config(state=NORMAL)
    Points.delete(1.8, END)
    Points.insert(1.8, New_Points)
    Points.config(state=DISABLED)
    global imgUrl
    pic_url = imgUrl
    my_page = urlopen(pic_url)
    my_picture = io.BytesIO(my_page.read())
    pil_img = Image.open(my_picture)
    tk_img = ImageTk.PhotoImage(pil_img)
    label = Label(root, image=tk_img, bg="#ed1a23")
    label.grid(row=0, column=0)
    root.mainloop()




GetHero()
Photo = PhotoImage(file="Questionmark.png")
Picture = Label(root, bg="#ed1a23", image=Photo)
Button_Submit = Button(root, text="Submit", padx=2, pady=15, font=("Calibri", 16), command=Submit )
Button_Next = Button(root, text="Next", padx=11, pady=15, font=("Calibri", 16), command=NextHero, state=DISABLED)
YourName = Entry(root, font=("Calibri", 14))
Hero = Entry(root, font=("Calibri", 16), width=24)
AskName = Label(root, text="Your name:", font=("Calibri", 12), bg='#ed1a23')
Points = Text(root, font=("Calibri", 30), bg="#ed1a23", height=1, bd=0)
What_is_that_superhero = Label(root, font=("Calibri", 16), text="Who's that superhero:", bg="#ed1a23")
Photo_time= PhotoImage(file="Time.png")
Picture_time= Label(root, bg="#ed1a23", image=Photo_time)
Points.insert(INSERT, "Points: 0")
Points.config(state=DISABLED)


Count_icon.place(x=250, y=210) #coordinaten voor de countdown
Button_Next.place(x=570, y=85)
AskName.place(x=160, y=5)
YourName.place(x=245, y=6)
Button_Submit.place(x=476, y=85)
Picture.place(x=0, y=0)
Hero.place(x=160, y=150)
Points.place(x=516, y=5)
What_is_that_superhero.place(x=160, y=115)
Picture_time.place(x=180, y=190)


Hint1button = Button(root, text="Hint 1", command = geefhint1, state=NORMAL)         #de knop om de hint in te drukken, dit activeert de geefhint1 functie
Hint1button.place(x=10, y=258)
output = Text(root, height = 1, width= 85,state=DISABLED)                                                                  #maakt de output tekst
output.place(x=60, y=258)                                                                   #zet de output naast de hint 1 button

Hint2button = Button(root, text="Hint 2", command = geefhint2)                       #de knop om de hint in te drukken, dit activeert de geefhint2 functie
Hint2button.place(x=10, y=300)
output2 = Text(root, height = 3, width= 85, state=DISABLED)                                                                 #maakt de output tekst
output2.place(x=60, y=290)                                                                #zet de output naast de hint 2 button

Hint3button = Button(root, text="Hint 3", command = geefhint3)         #de knop om de hint in te drukken, dit activeert de geefhint3 functie
Hint3button.place(x=10, y=345)
output3 = Text(root, height = 1, width= 85, state=DISABLED)                                                                 #maakt de output tekst
output3.place(x=60, y=350)                                                                #zet de output naast de hint 3 button

Hint4button = Button(root, text="Hint 4", command = geefhint4)         #de knop om de hint in te drukken, dit activeert de geefhint4 functie
Hint4button.place(x=10, y=380)
output4 = Text(root, height = 1, width= 85, state=DISABLED)                                                                 #maakt de output tekst
output4.place(x=60, y=380)                                                                #zet de output naast de hint 4 button

Hint5button = Button(root, text="Show Picture", command = geefhint5)         #de knop om de hint in te drukken, dit activeert de geefhint5 functie
Hint5button.place(x=10, y=418)
                                                              #zet de output naast de hint 5 button

Button_GiveUp = Button(root, text="Give up", padx=59, pady=15, font=("Calibri", 16), command=GiveUp)
Button_GiveUp.place(x=476, y=165)

root.mainloop()
