infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
def kaart(regels):
    for regel in regels:
        kaartinfo = regel.rstrip().split(',')
        print(max(kaartinfo))
kaart(regels)
infile.close()
