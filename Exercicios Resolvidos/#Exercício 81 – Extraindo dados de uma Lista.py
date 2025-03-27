#Exercício 81 – Extraindo dados de uma Lista#
lista=[]
opção=" "
while True:
    lista.append(int(input("Digite um numero na lista\n")))
    opção=str(input("Deseja continuar? S/N\n ")).strip().upper()  
    while opção not in "SN":
        opção=str(input("Deseja continuar? S/N\n ")).strip().upper()  
    if opção =="N":
        break
print(f"Foram digitados {len(lista)} numeros ")  
lista.sort()
lista.reverse()
print(f'A lista de valores digitadas em ordem decrescente é {lista}')
if 5 in lista:
    print("O valor 5 foi giditado e esta na lista")
else:
     print("O valor 5 não foi giditado e não esta na lista")


    