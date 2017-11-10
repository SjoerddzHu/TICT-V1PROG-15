temperatuur =  eval(input("hoeveel graden is het vandaag? "))

if temperatuur <= 15 and temperatuur > 0:
    print("het is koud vandaag")
elif temperatuur <= 0:
    print("het vriest")
else:
    print("het is warm vandaag")
