woord=''
while len(woord)!=4:
    woord = input('Geef een string van vier letters: ')
    if len(woord) != 4:
        print ('{} heeft {} letters'.format(woord,len(woord)))
print ('geslaagd')
