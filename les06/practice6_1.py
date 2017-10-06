def seizoen():
    maand = eval(input("welk maand nummer is het:"))
    if maand <= 5 and maand >= 3:
        print("lente")
    elif maand >= 5 and maand <= 8:
        print("zomer")
    elif maand >= 9 and maand <= 11:
        print("herfst")
    else:
        print("winter")
seizoen()
