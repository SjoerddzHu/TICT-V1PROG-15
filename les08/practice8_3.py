def code(invoerstring):
    nieuwestring=''
    for kar in invoerstring:
        nieuweASCII = ord(kar)+3
        nieuwekar = chr(nieuweASCII)
        nieuwestring += nieuwekar
    return nieuwestring
def uncode(invoerstring):
    nieuwestring=''
    for kar in invoerstring:
        nieuweASCII = ord(kar)-3
        nieuwekar = chr(nieuweASCII)
        nieuwestring += nieuwekar
    return nieuwestring
type = input('Wilt u code encrypten(e) of decrypten(d):')
inp = input('Voer een woord in:')
if type == 'e':
    print(code(inp))
elif type == 'd':
    print(uncode(inp))
else:
    print('Voer e of d in')
