def namen():
    namendict={}
    naam=input('Volgende naam')
    while naam !='':
        if naam in namendict:
            namendict[naam]+=1
        else:
            namendict[naam]=1
    for naam in namendict:
        if namendict[naam]==1:
            
