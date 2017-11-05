infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
for regel in regels:
    kaartinfo = regel.split(',')
    print('{} heeft kaartnummer {}:'.format(kaartinfo[1].strip(),kaartinfo[0]))



