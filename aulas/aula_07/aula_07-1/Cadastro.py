from Tabela import *


def adicionar():
    print("\nnovo cadastro")
    print("=============")
    x = 0
    while (x == 0):
        cadNome = str(input("digite o nome: "))
        cadIdade = str(input("digite a idade: "))
        cadSexo = str(input("digite o sexo: "))

        addTabela(cadNome, cadIdade, cadSexo)

        showTabela()

        print("\n Deseja novo cadastro?")
        x = int(input("sim - 0 | não - outros: "))
    menu()


def remover():
    print("\nremover cadastro")
    print("================")
    x = 0
    while (x == 0):
        linha = int(input("digite o numero da linha: "))

        delTabela(linha)

        showTabela()

        print("\n Deseja remover outro cadastro?")
        x = int(input("sim - 0 | não - outros: "))
    menu()
    
def atualizar():
    print("\natualizar cadastro")
    print("==================")
    x = 0
    while (x == 0):
        linha = int(input("digite o numero da linha: "))

        updateTabela(linha)

        showTabela()

        print("\n Deseja remover outro cadastro?")
        x = int(input("sim - 0 | não - outros: "))
    menu()
    
    


def menu():
    print("\nescolha a opção abaixo:")
    x = int(input("1 - adicionar cadastro | 2 - deletar cadastro | 3 - atualizar: "))
    if (x == 1):
        adicionar()
    
    if (x == 2):
        remover()
        
    if (x==3):
        atualizar()
        
    else:
        r = "\nprocesso concluido!"
        return r


menu()
