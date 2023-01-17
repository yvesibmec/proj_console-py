x = 1
while(x==1):
    print("\nEscolha uma das operacoes: ")
    x = int(input("1 - adicao(+)\n2 - subtracao(-)\n3 - multiplicacao(x)\n4 - divisao(÷)\n\n"))
    a = int(input("digite a: "))
    b = int(input("digite b: "))

    somar = lambda a, b: a + b
    subtração = lambda a , b:a - b
    multiplicação = lambda a , b:a * b
    divisão = lambda a , b:a/b

    if (x==1):
        print(somar(a,b))
    else:
        if (x==2):
            print(subtração(a,b))
        else: 
            if (x==3):
                print(multiplicação(a,b))
            else:
                if (x==4):
                    print(divisão(a,b))
                else:
                    print("operação não encontrada")
    x=int(input("deseja realizar novo calculo?\nSim - 1 | Não - 0:\n")) 

