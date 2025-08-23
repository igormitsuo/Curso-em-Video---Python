#Exercício 82 – Dividindo valores em várias listas#
listanum=[]
listpar=[]
listimpar=[]
cont=0
while True:
    listanum.append(int(input("Digite um numero na lista\n")))
    if listanum[cont] %2==0:
        listpar.append(listanum[cont])
        cont+=1
    else: 
       # listanum[cont] %2!=0
        listimpar.append(listanum[cont])
        cont+=1
    opção=str(input("Deseja continuar? S/N\n ")).strip().upper()  
    while opção not in "SN":
        opção=str(input("Deseja continuar? S/N\n ")).strip().upper()  
    if opção == "N":
        break
print(listanum)
print(listpar)
print(listimpar)