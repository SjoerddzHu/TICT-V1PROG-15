bruin=('Boxtel','Best','Beukenlaan','Eindhoven','Helmond \'t Hout','Helmond','Helmond Brouwhuis','Deurne')
groen=('Boxtel','Best','Beukenlaan','Eindhoven','Geldrop','Heeze','Weert')
for bruin1 in bruin:
    for groen1 in groen:
        if bruin1 == groen1:
            print (bruin1)
x=0
print()
for bruin1 in bruin:
    number = 0
    if groen[number] != bruin[number]:
        print (bruin1)
        number+=1
