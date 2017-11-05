invoer="5-9-7-1-7-8-3-2-4-8-7-9"
stringgetal=invoer.split('-')
stringgetal.sort()

getallenlijst=[]
for stringetal in stringgetal:
    getal=int(stringetal)
    getallenlijst.append(getal)

print('Gesorteerde list van ints: ',getallenlijst)
print('grootste getal:', max(stringgetal))
print('kleinste getal:', min(stringgetal))

som=0
for i in range (len(stringgetal)):
    som=som+int(stringgetal[i])
print('aantal getallen: ', len(stringgetal), 'en Som van de getallen: ', som)
print('gemiddelde: ', som / len(stringgetal))

