#Exercício 58 – Jogo da Adivinhação v2.0#
import random  
import time
cont=0
print(" estou pensando em uma numero de 0 a 10, consegue adivinhar?")
jogo=[0,1,2,3,4,5,6,7,8,9,10]
sorteio=random.choice(jogo)
#print(" {}".format(sorteio))
numero=int(input("qual o numero que eu pensei "))
print("Processando.....")
time.sleep(1)
while numero != sorteio:
    if numero != sorteio:
        print("errrroooooouuuuuuuuuuu!!!!!")
        print("tente de novo")
        cont+=1
        dica=str(input(" voce deseja uma dica? S / N ")).strip().upper()[0]
        if dica in "Ss":
            if numero > sorteio:
                print("o numero é menor que o digitado ")
            elif numero < sorteio:
                print(" o numero é maior que o digitado")
    numero=int(input("qual o numero que eu pensei "))
    print("Processando.....")
    time.sleep(1)
print("parabens, voce acertou! levou {} vezes para acertar".format(cont) )