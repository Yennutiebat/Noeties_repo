"""
Schrijf (en test) functie wijzig() met één parameter:
letterlijst. Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde! Test je programma als volgt:
lijst = ['a', 'b', 'c'] print(lijst) wijzig(lijst) print(lijst)
"""
lijst=[1,2,3]
def wijzig(letterlijst):
    letterlijst=[]
    letterlijst.append("d")
    letterlijst.append("e")
    letterlijst.append("f")
    print(letterlijst)
print(lijst)
wijzig(lijst)
print(lijst)
