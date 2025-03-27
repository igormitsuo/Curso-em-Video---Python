#Exercício 78 – Maior e Menor valores na Lista#
num=list()
for cont in range (0,5):
    num.append(int(input("entre com um numero ")))
print(f"a lista digitada foi {num}")
print(f"o maior numero foi {max(num )}, na porisção {num.index(max(num))} e o menos num foi{min(num)} na posição {num.index(min(num))}")