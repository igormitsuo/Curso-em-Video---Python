#Exercício 61 – Progressão Aritmética v2.0#
print(" gerador de PA")
print("-="*30)
primeiro=int(input(" entre com o primeiro termo da PA: "))
razão=int(input("entre com a razão da PA: "))
termo=primeiro
cont=1
while cont<=10:
    print("{}-> ".format(termo),end="")
    termo +=razão
    cont+=1
print("fim")
