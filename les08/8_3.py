naam = input("geef hier je naam in: ")
beginstation = input("geef hier je begin station: ")
eindstation = input("geef hier je eindstation: ")

geheleString = ""
eindstring = ""
geheleString += naam + beginstation + eindstation
print(geheleString)
for x in geheleString:
    nieuweASCII = ord(x) + 3
    nieuwekar = chr(nieuweASCII)
    eindstring += nieuwekar

print(eindstring)
