#Exercício 47 – Contagem de pares#
inicio=int(input("entre com numero de inicio da contagem "))
fim=int(input("entre com o numero final da contagem "))
fim+=1
for num in range(inicio,fim):
    if num %2==0:
        print(num, end=' ')
    else: print("")
print("acabou")