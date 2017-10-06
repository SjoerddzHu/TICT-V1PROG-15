zin = 'all animals are equal but some are more equal than others'
woorden = zin.split(' ')
woordenteller = {}
for woord in woorden:
    if woord in woordenteller.keys():
        woordenteller[woord] += 1
    else:
        woordenteller[woord] = 1
    print('{:7} komt {} keer voor.'.format(woord, woordenteller[woord]))
