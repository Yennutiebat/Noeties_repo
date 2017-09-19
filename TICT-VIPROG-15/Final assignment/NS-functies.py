def standaardprijs(afstandKM):
    if afstandKM>50:
        prijs=afstandKM*0.6+15
    elif afstandKM<=0:
        prijs=0
    else:
        prijs=afstandKM*0.8
    return prijs


def ritprijs(leeftijd,weekendrit,afstandKM):
    prijs=standaardprijs(afstandKM)

    if weekendrit == False:
        if leeftijd < 12 or leeftijd>=65:
            prijs=prijs*0.7
            return prijs
        else:
            prijs=prijs*1
            return prijs


    elif weekendrit == True:
        if leeftijd < 12 or leeftijd>=65:
            prijs=prijs*0.65
            return prijs
        else:
            prijs=prijs*0.6
            return prijs


print(ritprijs(11,False,49))
print(ritprijs(11,False,50))
print(ritprijs(11,False,51))
print(ritprijs(11,True,51))
print(ritprijs(12,False,49))
print(ritprijs(12,False,50))
print(ritprijs(12,False,51))
print(ritprijs(12,True,51))
