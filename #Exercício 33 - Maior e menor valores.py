#Exercício Python #033 - Maior e menor valores#
a=float(input("entre com o 1º valor "))
b=float(input("entre com o 2º valor "))
c=float(input("entre com o 3º valor "))
#verificando quem é o menor
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
# verificando quem é o maior
maior=a
if b>a and b>c:
   maior=b
if c>a and c>b:
   maiorr=c
print("o menor valor é {}".format(menor))
print("o maior valor é {}".format(maior))


