try:
    numlist = [100, 101, 0, '103', 104]
    index = int(input('geef een index:'))
    print(100/numlist[index])
except ValueError:
    print("er gaat iets fout")
except ZeroDivisionError:
    print("je mag niet met 0 delen domme k*t")
except TypeError:
    print("de lijst bevat een niet numeriek element")
except IndexError:
    print("je moet een getal tussen -5 en 4 invoeren")
