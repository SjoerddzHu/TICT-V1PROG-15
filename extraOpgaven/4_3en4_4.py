beginbedrag = eval(input("wat is je begin bedrag? "))
rentepercentage = eval(input("wat is het rentepercantage? "))

def eindbedrag():
    rentebedrag = beginbedrag / 100 * rentepercentage
    eindbedrag = beginbedrag + rentebedrag
    print(rentebedrag)
    return eindbedrag
x = eindbedrag()

print(x)
