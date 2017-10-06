def lijst():
 zin = eval(input("geef een lijst met minimaal 10 strings:(of gewoon 3 ofzo 10 is zo veeellll)"))
    for woord in zin:
        if woord.length >= 4:
            return woord
lijst()
