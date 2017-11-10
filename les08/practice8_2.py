import random
dobbelsteen2 = 0
dobbelsteen1 = 1
while dobbelsteen2 != dobbelsteen1:
    dobbelsteen1 = random.randrange(1,7)
    dobbelsteen2 = random.randrange(1,7)
    som = dobbelsteen1 + dobbelsteen2
    print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, som))
    if dobbelsteen2 == dobbelsteen1:
