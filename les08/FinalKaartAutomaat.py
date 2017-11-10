stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Ámsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'denbosch', 'einhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstation = input("wat is je beginstation, kies uit de lijst hierboven: ")
    if beginstation in stations:
        return beginstation and inlezen_eindstation(stations,beginstation)

    else:
        print(beginstation, " station staat niet in de lijst ")
        inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    eindstation = input("Wat is je eindstation, kies weer uit de lijst, let op het station moet na je ingevoerde station komen: ")
    if eindstation in stations and stations.index(eindstation) > stations.index(beginstation):
        return eindstation and omroepen_reis(stations, beginstation, eindstation)
    else:
        print("je ingevoerde station klopt niet, probeeer opnieuw")
        inlezen_beginstation(stations)

def omroepen_reis(stations,beginstation,eindstation):
    beginstationIndex = stations.index(beginstation)
    eindstationIndex = stations.index(eindstation)
    verschil = eindstationIndex - beginstationIndex
    ritprijs = verschil * 5
    tussenstations = ""
    print(beginstation, beginstationIndex)
    print(eindstation, eindstationIndex)
    print("de afstand is ", verschil)
    print("je ritprijs is ", ritprijs)
    for i in range(beginstationIndex + 1, eindstationIndex):

        tussenstations += stations[i] + ", "
    # goedetussenstations = tussenstations - beginstation
    print("je reis begint in", beginstation, "en je tussnestations zijn", tussenstations, "en je eindigt in", eindstation)

beginstation = inlezen_beginstation(stations)
# eindstation = inlezen_eindstation(stations, beginstation)
# omroepen_reis(stations, beginstation,eindstation)
