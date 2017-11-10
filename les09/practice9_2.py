import csv

with open('newfile.csv','w',newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input("wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("wat zijn je voorletters? ")
        gbdatum = input("wat is je geboortedatum? ")
        email = input("wat is je email? ")

        writer.writerow((naam,voorl,gbdatum,email))
