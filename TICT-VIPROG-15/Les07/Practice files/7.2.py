invoer=''

while len(invoer) !=4:
    if len(invoer)==4:
        break
    invoer=input('geef een woord: ')
    print(invoer+' heeft '+str(len(invoer))+' letters')
print('Inlezen van correcte string: '+invoer+' is geslaagd')
