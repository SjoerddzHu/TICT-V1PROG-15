grondgetallen = [4, 5, 3, -81]
def kwadraten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
       if getal >= 0:
           som = som +(getal**2)
    return som

print(str(kwadraten_som(grondgetallen)))
