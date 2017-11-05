def ticker():
    infile=open('bedrijven.txt','r')
    regels=infile.readlines()
    infile.close()
    tickerdict={}
    for regel in regels:
        tickerregel=regel.split(':')
        sleutel=tickerregel[0]
        waarde=tickerregel[1].strip()
        tickerdict[sleutel]=waarde
    return tickerdict


tickerbestand=ticker()
code=input('Afkorting: ')
for naam in tickerbestand:
    if code==tickerbestand[naam]:
        print(naam)


bedrijfnaam=input('Geef een bedrijf: ')
for naam in tickerbestand:
    if naam==bedrijfnaam:
        print(tickerbestand[naam])
