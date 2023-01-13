import math


def entrada_1():
    v1 = int(input("\nDigite nº1: "))
    return v1

def entrada_2():
    v2 = int(input("Digite nº2: "))
    return v2

class Calculo:
    
    def switch(self,operacao):
        default = "nao encontrado"
        return getattr(self,'case_'+str(operacao),lambda:default)()

    def case_1(self):
        rest = int(entrada_1()%entrada_2())
        return rest
    
    def case_2(self):
        med = round(float((entrada_1()+entrada_2())/2),2)
        return med
    
    def case_3(self):
        pot = round(float(pow(entrada_1(),entrada_2())),2)
        return pot
    
    def case_4(self):
        raiz = round(float(entrada_1()**(1/entrada_2())),2)
        return raiz
    
    def case_5(self):
        porc = str(round(float((entrada_1()/entrada_2())*100),2))+"%"
        return porc
    
def menu():
    x=1
    while(x==1):
        s = Calculo()
        print("\nEscolha a operacao: ")
        opcao = int(input("1 - resto(%)\n2 - med\n3 - pot\n4 - raiz\n5 - porc(%)\n\n"))
        print("\n o valor do resultado é:",s.switch(opcao))
        x = int(input("\nDeseja realizar nova conta?\n Sim - 1 | Não - 0: "))
        
menu()

