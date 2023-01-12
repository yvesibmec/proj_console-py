from Pessoa import *

cadastro = []
y = 0


def adicionar():
    x = 1
    y = len(cadastro)+1
    while (x == 1):
        nome = str(input("\ndigite o nome: "))
        idade = str(input("digite a idade: "))
        sexo = str(input("digite o sexo: "))

        cadastro.append(Pessoa(y, nome, idade, sexo))
        mostrar()
        y += 1
        x = int(input("\ndeseja novo cadastro?\nsim - 1 | nao - 0: "))
    menu()


def mostrar():
    print("{:<5}{:<10}{:<7}{:<5}".format("\nNº", "Nome", "Idade", "Sexo"))
    print("=========================")
    for v in cadastro:
        print("{:<5}{:<10}{:<7}{:<5}".format(v.get_id(),
              v.get_nome(), v.get_idade(), v.get_sexo()))


def alterar(y, x):
    y -= 1
    if (x == 1):
        nome = str(input("\ndigite o nome: "))
        cadastro[y].set_nome(nome)
        mostrar()

    if (x == 2):
        idade = str(input("\ndigite a idade: "))
        cadastro[y].set_idade(idade)
        mostrar()

    if (x == 3):
        sexo = str(input("\ndigite o sexo: "))
        cadastro[y].set_sexo(sexo)
        mostrar()


def menu():
    if (len(cadastro) == 0):
        adicionar()
    else:
        r = int(input("\nescolha uma opção:\n1 - Adicionar\n2 - Alterar\n "))
        if (r == 1):
            adicionar()
        if (r == 2):
            linha = int(input("digite o nº da linha: "))
            item = int(
                input("escolha a opção\n1 - nome\n2 - idade\n3 - sexo\n"))
            alterar(linha, item)
        else:
            r = "\nOpção não encontrada. Finalizando o programa..."
            return r


menu()
