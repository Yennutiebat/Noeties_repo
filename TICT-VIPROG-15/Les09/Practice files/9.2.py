import csv

with open('inloggers.csv','w',newline='') as myCSVfile:
    writer=csv.writer(myCSVfile,delimiter=';')

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((naam,voorl,gbdatum,email))
