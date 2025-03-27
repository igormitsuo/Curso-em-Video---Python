#Exercício 59 – Criando um Menu de Opções#
import random  
import time
n1=int(input(" entre o 1º numero "))
n2=int(input(" entre o 2º numero "))
opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
while opção!= 5: 
    if opção ==1:
        print("-"*30)
        print("a soma de {} e {} é {}".format(n1,n2,n1+n2))
        print("-"*30)
        opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
    if opção ==2:
        print("-"*30)
        print("a multiplicação de {} e {} é {}".format(n1,n2,n1*n2))
        print("-"*30)
        opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
    if opção ==3:
        print("-"*30)
        if n1>n2:
            print("o maior entre os dois é {}".format(n1))
        print("-"*30)
        print("-"*30)
        if n2>n1:
            print("o maior entre os dois é {}".format(n2))
        print("-"*30)
        print("-"*30)
        if n2==n1:
            print("os dois são iguais")
        print("-"*30)            
        opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
    if opção ==4:
        print("entre com novos numero")
        n1=int(input(" entre o 1º numero "))
        n2=int(input(" entre o 2º numero "))
        opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
    if opção>5:
        print("-"*30)
        print(" OPÇÃO INVALIDA, DIGITE NOVAMENTE")
        print("-"*30)
        opção=int(input(" escolha a opção desejada \n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR ENTRE OS 2 \n [ 4 ] NOVOS NUMERO \n [ 5 ] SAIR DO PROGRAMA \n  "))
    else: opção==5 
print("finalizando")     
time.sleep(1)
print("obrigado")


        


