
def volledigesom(getallenrij):
    print("de som van de rij is ", sum(getallenrij))
    eindgetal = 0
    for x in getallenrij:
        if x % 2 == 0:
            eindgetal += x
    return eindgetal


def onevensom(getallenrij):
    eindgetaloneven = 0
    for g in getallenrij:
        if g % 2 != 0:
            eindgetaloneven += g
    return eindgetaloneven

getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
y = volledigesom(getallenrij)
z = onevensom(getallenrij)


print("de som van even getallen is", y)
print("de som van de oneven getallen is", z)
print("de volledige som", y + z)
