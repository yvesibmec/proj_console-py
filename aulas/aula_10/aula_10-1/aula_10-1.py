microcamp = []
cadastro = {}
x=1
while(x==1):
    cadastro['escola']=str(input("\ndigite a escola: "))
    cadastro['curso']=str(input("digite o curso: "))
    cadastro['ativo']=bool(input("digite a situação: "))
    microcamp.append(cadastro)
    x = int(input("\nDeseja novo cadastro?\nSim - 1 | Não - 0: "))
    for i in range(0,len(microcamp),1):
        print(microcamp)
    
    
    
    
        
    

    
    
    
    
    
    
    
    
    
    
    



