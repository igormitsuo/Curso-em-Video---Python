#Exercício 79 – Valores únicos em uma Lista#
listanum=[]
opção=" "
while True:
    num=int(input("Entre com um numero\n"))
    if num in listanum:
        print("Esse numero já existe") 
    else:
        listanum.append(num)    
        opção=str(input("Deseja continuar? S/N\n ")).strip().upper()
    while opção not in "SN":
        opção=str(input("Deseja continuar? S/N\n ")).strip().upper()  
    if opção =="N":
        break
listanum.sort()
print(listanum)

    