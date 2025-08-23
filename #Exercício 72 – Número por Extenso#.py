#Exercício 72 – Número por Extenso#
cont=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","dose","treze","quatorze","quinze","desesseis","desesete","desoito","desenove","vinte")
escolha=" "
#num=int(input("entre com um numero entre 0 e 20\n "))
#minha resolução:
'''while num not in range (0,20):
    print("numero invalido, digite novamente: ")
    num=int(input("entre com um numero entre 0 e 20\n "))
print(f"voce digitou o numero: {cont[num]}")'''
#resolução do guanabara
'''while True:
    num=int(input("entre com um numero entre 0 e 20\n "))
    if 0 <=num<=20:
        break
    print("tente novamente ",end=" ")
print(f"voce digitou o numero {cont[num]}")'''

#desafio 
while True:
    num=int(input("entre com um numero entre 0 e 20\n "))
    if num not in range (0,20):
        print("tente novamente ")
    else:
        print(f"voce digitou o numero {cont[num]}")
        escolha=str(input("deseja continuar S/N \n")).strip().upper()[0]    
    while escolha not in "SN":
        escolha=str(input("deseja continuar S/N \n")).strip().upper()[0]
    if escolha in "N":
         break
print("ok, obrigado")



