lijst=input("Geef lijst met minimaal 10 strings: ")
nieuwelijst=lijst.split(' ')
for i in range (len(nieuwelijst)):
    if len(nieuwelijst[i])<4:
        print(nieuwelijst[i])
