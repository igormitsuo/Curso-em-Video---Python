#Exercício 84 – Lista composta e análise de dados Modelo 01#
cont=0
lista=[]
pesoleve=[]
pesopesado=[]
while True:
    nome=str(input("Entre com o nome do paciente:\n"))
    peso=int(input("Entre com o peso do paciente:\n"))
    lista.append(nome)
    lista.append(peso)
    cont+=1
    if peso>100:
        pesopesado.append(nome)
        pesopesado.append(peso)
    else:
        pesoleve.append(nome)
        pesoleve.append(peso) 
    opção=str(input("Deseja continuar? S/N\n ")).strip().upper()
    if opção=="N":
        break

print(lista)
print(pesopesado)
print(pesoleve)
print(cont)
