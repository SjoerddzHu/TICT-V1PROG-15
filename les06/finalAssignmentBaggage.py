def toonaantalkleuzenvrij():
    infile= open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print(aantalvrij)
    infile.close()

def nieuwekluis():
    # maak een lijst met de getallen 1 tot en met 12 die de kluisnummers voorstellen
    kluisnummers = []
    for i in range (1, 13):
        kluisnummers.append(i)

    # het inlezen van kluizen.txt in een list kluizendata met readlines()
    # elk element van de lijst is een regel uit kluizen.txt
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()

    # alle regels van kluizendata worden doorlopen
    for kluis in kluizendata:
        # doorlopen van kluizendata en elke regel van kluizendata splitsen op ';'
        gegevensvan1kluis = kluis.split(';')
        # elke regel bestaat uit twee elementen waarvan het 1e element het nummer is;
        # let op: dit element komt uit een bestand en is dus een string, vandaar stringnummer
        stringnummer = gegevensvan1kluis[0]
        # stringnummer converteren naar een int en toekennen aan nummer
        nummer = int(stringnummer)
        # het element met de waarde nummer uit kluizendata verwijderen
        kluisnummers.remove(nummer)

    # nu bevat kluizendata alleen nummers die nog niet in gebruik zijn
    if len(kluisnummers) > 0:
        # pak het eerste element van kluizendata en dit is het nummer van de kluis
        nieuwkluisnummer = kluisnummers[0];
        # laat dit nummer aan de gebruiker weten
        print('Je kluisnummer is {}'. format(nieuwkluisnummer))
        # vraag de gebruiker om een code in te voeren
        code = input('Voer een code in: ')
        # open het bestand kluizen.txt om een nieuwe kluis toe te voegen met append
        outfile = open('kluizen.txt', 'a')
        # schrijf het nummer en de code in het tekstbestand gescheiden door een ';'
        # omdat append is gebruikt, worden nummer en code achteraan het bestand toegevoegd
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        # sluit het tekstbestand
        outfile.close()
    else:
        # alle kluizen zijn bezet
        print('Er is geen kluis meer beschikbaar')


def kluisopenen():
    infile= open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    stringnummer = input("wat is je nummer: ")
    code = input("wat is je code: ")
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringkluisnummer = gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringnummer == stringkluisnummer and code == kluiscode:
            gegevenscorrect = True
    if gegevenscorrect:
        print("de kluis wordt geopend: ")
    else:
        print("de kluis wordt niet geopend")
    infile.close()


print('1: hoeveel vrij')
print('2: nieuwe kluis')
print('3: kluis openen')

keuze = eval(input("maak je keuze: "))
if keuze == 1:
    toonaantalkleuzenvrij()
elif keuze == 2:
    nieuwekluis()
else:
    kluisopenen()
