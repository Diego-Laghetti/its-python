def esercizio4 (x,y,z):
    if x and (y or z) == True:
        return 'azione permessa'
    else:
        return 'azione negata' 
    
a = True
b = False
c = False
print(esercizio4(a, b, c))