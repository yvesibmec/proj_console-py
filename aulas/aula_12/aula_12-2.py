metros = [10,15,47,85,96,12,74,32,65,50]
metros.sort()
polegadas = [round(x*39.37,2) for x in metros]
pes = [round(x*3.28,2) for x in metros]
jardas = [round(x*1.09,2) for x in metros]
milhas = [round((x*0.6214)/1000,3) for x in metros]

print ("{:<4}{:<9}{:<12}{:<9}{:<9}{:<8}".format("Nº", "Metros", "Polegadas", "Pes", "Jardas", "Milhas"))
print("=================================================")
for v in range(0,len(metros),1):
    print ("{:<4}{:<9}{:<12}{:<9}{:<9}{:<8}".format(v, metros[v], polegadas[v], pes[v], jardas[v], milhas[v]))
     