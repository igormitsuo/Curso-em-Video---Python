#Exercício Python #019 - Sorteando um item na lista#
import random
a=str(input("entre com o nome do primeiro aluno"))
b=str(input("entre com o nome do segundo aluno"))
c=str(input("entre com o nome do terceiro aluno"))
d=str(input("entre com o nome do quarto aluno"))
print("o aluno sorteado é {}".format(random.choice([a,b,c,d])))
