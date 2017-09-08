x=100

if x == 1000:
   print("wtffffffff")
else:
   print("hello world")

'5'
sorted('Berlioz''Borodin''Brian')

papier = 'papier'
nietjes = 'nietjes'
pennen = 'pennen'
inventaris= papier + ' '+ nietjes +' '+ pennen
print(inventaris)
print(len(inventaris))

voornaam='sjoerd'
achternaam='de zaaijer'
mijnnaam = voornaam + ' ' + achternaam
print(mijnnaam)
print(len(mijnnaam))

if len(inventaris) / 5 > len(mijnnaam):
    print("ik ben 5x groter dan mijn naam ")
else:
    print('ik ben niet 5x groter dan mijnnaam')

if inventaris == [] or len(inventaris) > 10:
    print('een van deze is correct')

a = 6.00
b = 7
c = 6.75

p = c > a
print(p)

y = c < b
print(y)


favorieten = ['Ken']
favorieten.append('Eminem')
print(favorieten)
favorieten[1] ='barbie'
print(favorieten)

getallen = [1,1, -10, -100]
print(max(getallen) - min(getallen))
