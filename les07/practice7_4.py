def ticker():
    infile = open('ticker.txt','r')
    regels = infile.readlines()
    infile.close()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict
tickerdict = ticker()
bedrijfsnaam = input('Geef een bedrijfsnaam: ')
for naam in tickerdict:
    if naam == bedrijfsnaam:
        print(tickerdict[naam])
bedrijfsticker = input('Geef een ticker-symbool: ')
for naam in tickerdict:
    if naam == bedrijfsticker.strip:
        print(tickerdict)
