#Exercício 55 – Maior e menor da sequência#
maior=0
menor=0
for p in range (1,6):
    peso=float(input("peso da {}º pessoa ".format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("o maior peso lido foi {} kg".format(maior))
print("o menorr peso lido foi {} kg".format(menor))

