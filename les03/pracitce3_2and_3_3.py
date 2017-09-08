naam = input("Wat is je naam: ")
leeftijd = eval(input("wat is je leeftijd: "))
pasport = input("heb je een paspoort, beantwoord alleen met ja of nee: ")
print("je naam is " + naam + ", je leeftijd is ", leeftijd, " volgend jaar ben je", leeftijd + 1)
if leeftijd>= 18 and pasport== "ja":
    print(naam + " je mag stemmen!")
else:
    print(naam + " je mag niet stemmen1")
