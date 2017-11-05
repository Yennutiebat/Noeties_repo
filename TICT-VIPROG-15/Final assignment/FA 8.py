stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch',
            'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstation = input('Geef beginstation: ')
    while beginstation not in stations:
        beginstation = input('Niet correct. Geef beginstation: ')
    return beginstation

def inlezen_eindstation(stations,beginstation):
    eindstation = input('Geef eindstation: ')
    while eindstation not in stations:
        eindstation = input('Niet correct. Geef eindstation: ')
        while stations.index(eindstation)>stations.index(beginstation):
            eindstation=input('fout geef iets dergelijkst')
        return eindstation

def omroepen_reis(stations,beginstation,eindstation):
    nummerB=stations.index(beginstation)+1
    nummerE=stations.index(eindstation)+1
    print('Het beginstation is {} Het eindstation is {}'.format(beginstation,nummerB))
    afstand=nummerE-nummerB
    prijs=5*afstand
    for index in range(nummerB,nummerE-1):
        print(stations[index])

inlezen_eindstation(stations,inlezen_beginstation(stations))
