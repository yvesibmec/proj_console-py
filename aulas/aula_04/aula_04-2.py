print("faça uma soma: \n")
valor1 = int(input("digite nº1:"))
valor2 = int(input("digite nº2:"))

def soma(x,y):
    resultado = x + y
    return resultado

print("o resultado da soma é:",soma(valor1,valor2))


print("faça uma subtração: \n")
n1 = int(input("digite o primeiro valor:"))
n2 = int(input("digite o segundo valor"))

def subtração(x,y):
    resultado = x - y
    return resultado

print("o resultado da subtração é:",subtração(n1,n2))

print("faça uma divisão: \n")
n1 = int(input("digite o primiro numero:"))
n2 = int(input("digite o segundo numero:"))

def divisão(x,y):
    resultado = x/y
    return resultado

print("o resultado da divisão é:",divisão(n1,n2))
