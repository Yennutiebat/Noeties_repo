print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen=len(kluizendata)
    aantalvrij=12-aantalkluizen
    print(aantalvrij)

def nieuwe_kluis():
    kluisnummers = []
    for i in range (1, 13):
        kluisnummers.append(i)

    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()

    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringnummer = gegevensvan1kluis[0]
        nummer = int(stringnummer)
        kluisnummers.remove(nummer)

    if len(kluisnummers) > 0:
        nieuwkluisnummer = kluisnummers[0];
        print('Je kluisnummer is {}'. format(nieuwkluisnummer))
        code = input('Voer een code in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        outfile.close()
    else:
        print('Er is geen kluis meer beschikbaar')

def kluis_openen():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer=input('geef een kluisnummer: ')
    code=input('wat is je code: ')
    gegevenscorrect=False
    for kluis in kluizendata:
        gegevensvan1kluis=kluis.split(';')
        stringkluisnummer=gegevensvan1kluis[0]
        kluiscode=gegevensvan1kluis[1].strip()
        if stringnummer==stringkluisnummer and code == kluiscode:
            gegevenscorrect=True
    if gegevenscorrect:
        print('kluis is geopend')
    else:
        print('kluis of wachtwoord incorrect')

def kluis_teruggeven():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is het nummer van je kluis: ')
    code = input('Wat is de code van je kluis: ')
    nieuwekluizendata = []
    for kluis in kluizendata:
        datavan1kluis = kluis.split(';')
        stringkluisnummer = datavan1kluis[0]
        kluiscode = datavan1kluis[1].strip()
        gegevenscorrect = (stringkluisnummer == stringnummer) and (kluiscode == code)
        if not gegevenscorrect:
            nieuwekluizendata.append(stringkluisnummer + ';' + kluiscode)

    outfile = open('kluizen.txt', 'w')
    for i in range(0, len(nieuwekluizendata)):
        outfile.write(nieuwekluizendata[i] + '\n')
    outfile.close()



keuze = eval(input('geef een keuze: '))
if keuze==1:
        toon_aantal_kluizen_vrij()

elif keuze==2:
        nieuwe_kluis()

elif keuze==3:
        kluis_openen()

elif keuze==4:
        kluis_teruggeven()
else:
        print('u heeft geen geldige optie gekozen')



