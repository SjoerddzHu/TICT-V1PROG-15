
try:
    kosten = 4356
    aantal = eval(input("met hoeveel mensen zijn jullie? "))
    if aantal < 0:
        print("je mag niet delen met min getallen")
    else:
        print("kosten zijn:", kosten/aantal)
except ZeroDivisionError:
    print("delen door 0 kan niet")
except NameError:
    print("je mag niet delen met woorden, gebruik cijfers")


