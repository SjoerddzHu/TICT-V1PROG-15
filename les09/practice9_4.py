import csv

with open('producten.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('ArtikelNummer', 'ArtikelCode', 'Naam', 'Voorraad', 'Prijs'))
    while True:
        artikelnummer = input("Wat is het artikelnummer: ")
        if artikelnummer == "einde":
            break
        ArtikelCode = input("Wat is het artikelcode: ")
        Naam = input("Wat is de naam: ")
        Voorraad = input("Hoeveel voorraad is er: ")
        Prijs = input("Wat is de prijs: ")
        writer.writerow((artikelnummer, ArtikelCode, Naam, Voorraad, Prijs))
