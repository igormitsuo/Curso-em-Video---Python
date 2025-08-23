#Exercício Python #020 - Sorteando uma ordem na lista#
import random
a=str(input("entre com o nome do primeiro aluno "))
b=str(input("entre com o nome do segundo aluno "))
c=str(input("entre com o nome do terceiro aluno "))
d=str(input("entre com o nome do quarto aluno "))
lista=[a,b,c,d]
random.shuffle(lista)
print("a rodem de apresentação é {}".format(lista))