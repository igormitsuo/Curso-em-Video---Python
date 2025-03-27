#Exercício 45 – GAME: Pedra Papel e Tesoura#
import random
import time
print("="*15,"JOGO JOKENPO","="*15)
print(''' suas opções: 
      [ 1 ] pedra
      [ 2 ] papel
      [ 3 ] tesoura''')
opção=int(input(" qual sua opção de jogada "))
if opção !=1 and opção!=2 and opção!=3:
    print(" opção invalida")
else:   
    print("JO.....")
    time.sleep(1)
    print("KEN.....")
    time.sleep(1)
    print("PO.....")
    time.sleep(1)
    print("="*30)
    comp=[1,2,3]
    sorteio=random.choice(comp)
    if opção==1 and sorteio==1:
        print("o computador escolheu pedra e voce escolheu pedra - empatou")
    elif opção==1 and sorteio==2:
        print("o computador escolheu papel e voce escolheu pedra - computador ganhou")
    elif opção==1 and sorteio==3:
        print("o computador escolheu tesoura e voce escolheu pedra - voce ganhou")
    elif opção==2 and sorteio==2:
        print("o computador escolheu papel e voce escolheu papel - empatou")
    elif opção==2 and sorteio==1:
        print("o computador escolheu pedra e voce escolheu papel - voce ganhou")
    elif opção==2 and sorteio==3:
        print("o computador escolheu pedra e voce escolheu tesoura - computador ganhou")
    elif opção==3 and sorteio==3:
        print("o computador escolheu tesoura e voce escolheu tesoura - empatou")
    elif opção==3 and sorteio==1:
        print("o computador escolheu pedra e voce escolheu tesoura - computador ganhou")
    elif opção==3 and sorteio==2:
        print("o computador escolheu papel e voce escolheu tesoura - voce ganhou")



    
