#Exercício Python #023 - Separando dígitos de um número#
num=int(input("informe um numero "))
n=str(num)
print("analisando o numero {}".format(num))
print("unidade {}.".format(n[3]))
print("dezena {}.".format(n[2]))
print("centena {}.".format(n[1]))
print("milhar {}.".format(n[0]))
