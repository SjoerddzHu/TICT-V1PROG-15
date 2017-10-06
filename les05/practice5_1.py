def convert(celsius):
    farhenheit = celsius * 1.8 + 32
    return farhenheit

def table():
    print('{:^8} {:^8}'.format('F', 'C'))
    for c in range(-30, 41, 10):
       print('{:^8} {:^8}'.format(convert(c), c))
table()
