#Exercício 68 – Jogo do Par ou Ímpar#
import random    
resultado=""
cont=0
while resultado !="D":
    resultado=""
    maquina=0
    lista=[0,1,2,3,4,5,6,7,8,9,10]
    print("-="*15 )
    print(f"vamos jogar par ou impar! ")
    print("-="*15 )
    num=int(input("digite um numero de 0 a 10 \n"))
    if num in range (0,11):
        print("-="*15 )
        opção=str(input("par ou impar ?\n")).upper().strip()[0]
        print("-="*15 )
        maquina=random.choice (lista)        
    elif print("opção invalida"):
         print("-="*15 )
         break    
    if opção=="P":
        valor=(num+maquina)%2==0
        print("-="*15 )
        print("parabens voce ganhou!")
        print(f"voce jogou {num} e a maquina jogou {maquina} o resultado foi {num+maquina} vamos de novo!")
        print("-="*15 )
        resultado="v"
        cont+=1
    elif opção=="I":
        valor=(num+maquina)%2==0
        resultado="F"
        break
print(" voce perdeu")
print(f"-="*15 )
print(f"voce jogou {num} e a maquina jogou {maquina} o resultado foi {num+maquina} ")
print(f"-="*15 )
print(f"voce ganhou {cont} vezes seguidas")

