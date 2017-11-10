getallen=[1,2,3,4,5,6,7,8,9,10]
for eerste in (getallen):
    for tweede in (getallen):
        print('{} x {} = {}'.format(tweede, eerste, eerste*tweede))
