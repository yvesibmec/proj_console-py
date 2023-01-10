import math

def pitágoras(x):
    if(x==1):
        b = int(input("digite b:"))
        c = int(input("digite c:"))
        a = round(math.sqrt(pow(b,2)+pow(c,2)),2)
        return a
    else:
        if(x==2):
            a = int(input("digite a:"))
            c = int(input("digite c:"))
            b = round(math.sqrt(pow(a,2)-pow(c,2)),2)
            return b
        else:
            a = int(input("digite a:"))
            b = int(input("digite b:"))
            c = round(math.sqrt(pow(a,2)-pow(b,2)),2)
            return c

print("\n{:<6}{:<6}".format("opção","busca"))
print("{:<6}{:<6}".format(1,"a"))
print("{:<6}{:<6}".format(2,"b"))
print("{:<6}{:<6}".format(3,"c"))
x = int(input("digite uma opção:"))
print(pitágoras(x),"\n")


              

