def code(invoerstring):
    nieuwestring=''
    for kar in invoerstring:
        nieuweACII=ord(kar)+3
        nieuwekar=chr(nieuweACII)
        nieuwestring+=nieuwekar
    return nieuwestring
naam=input('geef naam: ')
beginstation=input('geef beginstation: ')
eindstation=input('geef eindstation: ')
uitvoerstring=code(naam)
print(uitvoerstring)
uitvoerstring=code(beginstation)
print(uitvoerstring)
uitvoerstring=code(eindstation)
print(uitvoerstring)
