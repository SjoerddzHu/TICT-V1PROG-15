afstandKM = eval(input("hoe veel km is je reis: "))
leeftijd = eval(input("wat is je leeftijd, antwoord in een cijfer: "))
weekendrit = input("is het weekend? antwoord met ja of nee: ")
def standaardprijs(afstandKM):

    if afstandKM <= 100:
        standaardprijs = 0.80 * afstandKM
        return standaardprijs

    elif afstandKM > 100:
            standaardprijs = 15 + (0.60 * afstandKM)
            return standaardprijs

    elif afstandKM < 0:
        standaardprijs = 0

standaardprijs(afstandKM)

def ritprijs(leeftijd, weekendrit, standaardprijs):

    if weekendrit == "ja" and leeftijd >= 65 or leeftijd <= 12 :
        korting = (standaardprijs / 100) * 35
        print(korting)
        print( standaardprijs - korting)

    elif weekendrit == "nee" and leeftijd >=65 or leeftijd <= 12 :
        korting = (standaardprijs / 100) * 30
        print(korting)
        print( standaardprijs - korting)

    elif weekendrit == "ja" and leeftijd >= 65 or leeftijd <=12 :
        korting = (standaardprijs / 100) * 40
        print("standaard prijs: ", standaardprijs)
        print("korting:", korting)
        print("eindprijs: ", standaardprijs - korting)

    elif weekendrit =="nee" and leeftijd <= 65 or leeftijd >=12:
        print("standaard prijs: ", standaardprijs)
        print("eindprijs: ", standaardprijs)
        return "je hebt geen recht op korting, je moet ", standaardprijs,"betalen"

ritprijs(leeftijd,weekendrit,standaardprijs(afstandKM))



