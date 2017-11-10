nummer=0
som = 0
getal=1
while getal != 0:
    getal = eval(input('Geef een getal: '))
    som += getal
    nummer+=1
print ('Er zijn {} getallen ingevuld, de som is: {}'.format(nummer,som))
