infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
for regel in regels:
    kaartinfo = regel.rstrip().split(',')
    print(kaartinfo[1] + " heeft kaartnummer: " + kaartinfo[0])


infile.close
