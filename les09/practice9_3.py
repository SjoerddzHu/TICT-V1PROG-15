import csv
with open('gamers.csv','r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    maximum = 0
    for row in reader:
        score = int(row[2])
        if score > maximum:
            maximum = score
            maxnaam = row[0]
            maxdatum = row[1]
    print("de hoogste score is",maximum,"behaald door ", maxnaam,"op ", maxdatum)



# with open('gamers.csv','r') as myCSVFile:
#     reader = csv.DictReader(myCSVFile, delimiter=';')
#     for row in reader:
#         print(row['name'],row['type'])
#
