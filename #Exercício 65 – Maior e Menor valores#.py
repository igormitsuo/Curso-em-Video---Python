#Exercício 65 – Maior e Menor valores#
cont=0
media=maior=0
num=int(input("entre com um numero "))
opção=str(input("deseja continuar [S/N ]")).strip().upper()[0]
soma=num
menor=num
cont+=1
while opção!="N":
    num=int(input("entre com um numero "))
    opção=str(input(" deseja continuar [S/N ]")).strip().upper()[0]
    cont+=1
    soma=soma+num    
    media=soma/cont     
    if maior<num:
        maior=num
    if menor>num:
        menor=num    
print(" o total de numeros digitados foi de {}, e a media entre eles é  {}".format(cont,media,))
print("o maior numero diagitado foi {} e o menor numero digitado foi {}".format(maior,menor))
