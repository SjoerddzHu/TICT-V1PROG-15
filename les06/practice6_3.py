variabele='9-5-7-1-7-8-3-2-4-8-7-9'
var=variabele.split('-')
var.sort()
som=0
max = (max(var))
min = (min(var))
len = (len(var))
for number in var:
    som+=int(number)
avg = som/len
print ('De gesorteerde lijst is {}'.format(var))
print ('De grootste waarde is: {}'.format(max))
print ('De kleinste waaarde is: {}'.format(min))
print ('De lengte van de lijst is: {}'.format(len))
print ('De som van de hele lijst is: {}'.format(som))
print ('Het gemiddelde van de lijst is: {}'.format(avg))
