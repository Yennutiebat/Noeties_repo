def convert(celcius):
    fahrenheit=celcius*1.8+32
    return fahrenheit

def table(celsiusrij):
    for temperaturen in celsiusrij:
        fahrenheit=convert(temperaturen)
        print(fahrenheit,temperaturen)

table([-30,-20,-10,0,10,20,30,40])
