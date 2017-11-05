try:
    bedrag=4356
    aantal=eval(input('geef bedrag: '))
    if aantal < 0:
        print('negatieve getallen zijn niet toegestaan')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    print('Delen door 0 kan niet')
except NameError:
    print('Gebruik cijfers')
except:
    print('Onjuiste invoer')
