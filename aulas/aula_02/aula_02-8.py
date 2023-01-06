nome = "Yves"
idade = 18
renda = 3500
entrada = 10000
serasa = False 
situação = True 

if(
    (idade>=18)
    and(renda>=2500)
    and(serasa==False)
):
    if(
        (renda>=5000)
        or(entrada>=10000)
    ):
        situação = True
        print("aprovado")
    else:
        print("analisar")
else:
    situação = False
    print("reprovado")
    