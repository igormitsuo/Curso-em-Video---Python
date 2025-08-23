#Exercício 70 – Estatísticas em produtos#
totgast=0
cont=contv=0
nomepb=nomep=" "
valor=0
while True:
    escolha=" "
    nomep=str(input("Entre com o nome do produto\n "))
    valorp=float(input("digite o valor do produto\n R$ "))
    contv+=1
    totgast+=valorp
    #da pra fazer dos dois jeitos
    if contv==1: #or valor > valorp:
      valor=valorp
      nomepb=nomep
      #print(f"{valor} {nomepb}")
       # valorp=valor
       # nomepb=nomep
        #print(f"{contv} {nomepb}")
    else:        
        if valor < valorp:
           nomep = nomepb   
           #print(f"{valor} {nomepb}") 
    if valorp>1000:
        cont+=1
    while escolha not in "SN":
        escolha=str(input("deseja continuar [S/N] ?\n ")).strip().upper()[0]
    if escolha=="N":
        break
print(f"o valor total gasto nas compra é de R$ {totgast:.2f}")
print(f"foram comprados {cont} produtos acima de R$ 1000.00")
print(f"o produto mais barado comprado é o {nomepb}")
    
