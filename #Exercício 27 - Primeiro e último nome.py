#Exercício Python #027 - Primeiro e último nome de uma pessoa#
n=str(input("digite seu nome ")).strip()
nome=n.split()
print(nome)
print(nome[0])
print(nome[len(nome)-1])
print("muito prazer, seu primeiro nome é {}".format(nome[0]))
print("seu ultimo nome é {}".format(nome[len(nome)-1]))