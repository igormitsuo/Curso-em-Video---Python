#Exercício 85 – Listas com pares e ímpares resolução meio guanabara meio igor#
listas=[[],[]]
for c in range (1,8):
    num=int(input(f"Digite o {c}º numero\n ")) 
    if num %2==0:
        listas[0].append(num)
        listas[0].sort()
    else:
        num %2!=0
        listas[1].append(num)   
        listas[1].sort()      
print(f"os numeros pares digitados foram {listas[0]}")
print(f"os numeros impares digitados foram {listas[1]}")

