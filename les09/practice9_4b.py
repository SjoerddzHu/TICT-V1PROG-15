import csv

with open('producten.csv','r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    maxprijs = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > maxprijs:
            maxprijs = prijs
            maxnaam = row['Naam']
    print("het duurste product: ", maxprijs, "dit is: ", maxnaam)
