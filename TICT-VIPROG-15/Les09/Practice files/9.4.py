import csv

with open('bestand.csv','r',newline='') as myCSVfile:
    reader=csv.DictReader(myCSVfile,delimiter=';')
    duurste=0
    voorraad=1000000
    name=''
    totaal=0
    artikelnummer=0

    for row in reader:
        if float(row['Voorraad']) <float(voorraad):
            voorraad=row['Voorraad']
            artikelnummer=row['Artikelnummer']
        if float(row['Prijs']) > float(duurste):
            duurste=row['Prijs']
            name=row['Naam']
        totaal+=int(row['Voorraad'])
    print('Het duurste artikel is {} en die kost {} euro'.format(name, duurste))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {} '.format(voorraad,artikelnummer))
    print('In totaal hebben wij {} producten in ons magazijn liggen '.format(totaal))
