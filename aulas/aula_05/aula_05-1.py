import math

def bhaskara(a,b,c):
    delta = -b + 4*a*c
    if(a==0):
        resultado = "não é possível realizar operação. A = 0"
    else:
        if(delta<=0):
            resultado = "não é possível realizar operação. Delta <= 0"
        else:
            x1 = round((-b + math.sqrt(delta))/2*a,2)
            x2 = round((-b - math.sqrt(delta))/2*a,2)
            resultado = "o resultado é x1:",x1,"e x2: é:",x2
    return resultado

a = int(input("digite a:"))
b = int(input("digite b:"))
c = int(input("digite c:"))

print(bhaskara(a,b,c))
        