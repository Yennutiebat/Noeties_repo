infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()

regelnummer=0
grootstegetal=0


for regel in regels:
    regelnummer= regelnummer + 1
    info = regel.split(',')
    if int(info[0])>grootstegetal:
        grootstegetal=int(info[0])
        grootsteregelnmr=regelnummer

print(grootstegetal)
print('deze file telt ' + str(regelnummer) + ' regels')

