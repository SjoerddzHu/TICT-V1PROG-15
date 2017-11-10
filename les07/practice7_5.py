namendict = {}
while True:
    naam = input('Vul een naam in: ')
    if naam =='':
        break
    elif naam in namendict:
        namendict[naam] += 1
    else:
        namendict[naam] = 1
for naam in namendict:
    if namendict[naam] == 1:
        print('Er is {} student met de naam {}'.format(namendict[naam],naam))
    else:
        print('Er zijn {} studenten met de naam {}'.format(namendict[naam],naam))
