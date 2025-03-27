#Exercício 54 – Grupo da Maioridade#
from datetime import date
ano=date.today().year
maioridade=0
menoridade=0
for id in range(1,8):
    nasc=int(input("entre com a data de nascimento da {}º pessoa ".format(id)))
    idade=ano-nasc
    if idade>21:
        maioridade+=1
    else:
        menoridade+=1
print("ao todo tivemos {} pessoas maiores de idade".format(maioridade))
print("ao todo tivemos {} pessoas de menor ".format(menoridade))

'''meu codigo:

primeiro=int(input("entre com a data de nascimento da {}º pessoa ".format(id)))
    if ano-primeiro>18:
        maioridade+=1    
   segundo=int(input("entre com a data de nascimento da 2º pessoa "))
    if ano-segundo>18:
        maioridade+=1
    terceiro=int(input("entre com a data de nascimento da 3º pessoa "))
    if ano-terceiro>18:
        maioridade+=1
    quarto=int(input("entre com a data de nascimento da 4º pessoa "))
    if ano-quarto>18:
        maioridade+=1
    quinto=int(input("entre com a data de nascimento da 5º pessoa "))
    if ano-quinto>18:
        maioridade+=1
    sexto=int(input("entre com a data de nascimento da 6º pessoa "))
    if ano-sexto>18:
        maioridade+=1
    setimo=int(input("entre com a data de nascimento da 7º pessoa "))
    if ano-setimo>18:
         maioridade+=1
    else:
        minoridade+=1
    print(" foram {} maiores e {} menores".format(maioridade,minoridade))'''

    
