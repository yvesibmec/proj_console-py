from Pessoa import *
cadastro = []


def addTabela(a, b, c):
    cadastro.append(Pessoa(a, b, c))
    r = "\nusuario cadastrado com sucesso!"
    return r


def showTabela():
    print("{:<5}{:<10}{:<7}{:<5}".format("\nNº", "Nome", "Idade", "Sexo"))
    print("======================")
    x = 0
    for v in cadastro:
        print("{:<5}{:<10}{:<7}{:<5}".format(x, v.nome, v.idade, v.sexo))
        x += 1


def delTabela(x):
    print("\ndeseja remover ", cadastro[x].nome, " da tabela?")
    certeza = int(input("sim - 1 | não - outros: "))
    if (certeza == 1):
        del cadastro[x]
        r = "\nusuario removido com sucesso!"
        return r
    else:
        r = "\nação cancelada com sucesso!"
        return r


def updateTabela(x):
    print("deseja atualizar os dados de", cadastro[x].nome, "da tabela?")
    certeza = int(input("sim - 1 | não - outros: "))
    if (certeza == 1):
        option = int(
            input("\no que deseja alterar?\n1 - nome | 2 - idade | 3 - sexo:"))
        if (option == 1):
            cadastro[x].nome = str(int("digite o nome:"))
            r = "\nnome atualizado com sucesso!"
            return r
        
        if (option == 2):
            cadastro[x].idade = str(input("digite a idade:"))
            r = "\nidade atualizada com sucesso!"
            return r
            
        if (option==3):
            cadastro[x].sexo = str(input("digite o sexo:"))
            r = "\nsexo atualizado com sucesso!"
            return r
    else:
        r = "\nação cancelada com sucesso!"
        return r
