letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
alphabet = ['A','B','C']
list = list()

for chr in alphabet:
    list.append(letters.count(chr))
print(list)

