#Exercício 64 – Tratando vários valores v1.0#
cont=0
num=int(input("digite [999] para parar ou entre com um numero "))
soma=num
while num!=999:
    num=int(input("digite [999] para parar ou entre com um numero "))
    soma=soma+num
    cont+=1
print(" o total de numeros digitados foi de {}, e a soma foi de {}".format(cont,soma-999))
