#Exercício 75 – Análise de dados em uma Tupla#
num=(int(input("entre com um numero ")),int(input("entre com um numero ")),int(input("entre com um numero ")),
     int(input("entre com um numero ")))
print(num)
print(f"o numero 9 apareceu {num.count(9)} vezes")
print(f"o numero 3 aparece na {num.index(3,)+1}º posição")
if num[0]%2==0:
    print(num[0])
if num[1]%2==0:
    print(num[1])
if num[2]%2==0:
    print(num[2])
if num[3]%2==0:
    print(num[3])
else:
    print("não houve numeros pares")
