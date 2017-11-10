zin=input('Vul een zin in: ')
woorden = zin.split()
hoeveelheid =0
for letter in woorden:
    hoeveelheid=len(letter)+hoeveelheid
woorden=len(woorden)
antw=hoeveelheid/woorden
print(antw)
