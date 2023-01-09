x = 0
nome = []
idade = []
salario = []
ativo = []

while (x == 0):
    n = str(input("digite seu nome:"))
    i = int(input("digite sua idade:"))
    s = float(input("digite seu sálario:"))
    a = bool(input("digite se estiver ativo:"))
    if (a == 1):
        a = "ativo"
    else:
        a = "inativo"
        
    nome.append(n)
    idade.append(i)
    salario.append(s)
    ativo.append(a)
    y = len(nome)

    print("\n")
    print("{:<15}{:<7}{:<9}{:<9}"
        .format("nome", "idade", "salario", "atividade"))
    while (x < y):
        print("{:<15}{:<7}{:<9}{:<9}"
            .format(nome[x], idade[x], salario[x], ativo[x]))
        x += 1
    print("\n")
    x = int(input("deseja mais um cadastro: \n 0 - sim | 1 - não:"))


    
