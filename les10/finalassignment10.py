import xmltodict
def processXML(filename):
    with open(filename)as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

voorbeeldendict = processXML('Final assignment.xml')
voorbeelden = voorbeeldendict['Stations']['Station']
print('Dit zijn de codes en types van de {} stations'.format(len(voorbeelden)))
for voorbeeld in voorbeelden:
    print('{:4}- {}'.format(voorbeeld['Code'],voorbeeld['Type']))
print()
print('Dit zijn alle stations met een of meer synoniemen:')
for voorbeeld in voorbeelden:
    if voorbeeld['Synoniemen'] is not None:
        print('{:4}- {}'.format(voorbeeld['Code'],voorbeeld['Synoniemen']))
print()
print('Dit is de lange naam van elk station:')
for voorbeeld in voorbeelden:
    print('{:4}- {}'.format(voorbeeld['Code'],voorbeeld['Namen']['Lang']))