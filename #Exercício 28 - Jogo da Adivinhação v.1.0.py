#Exercício Python #028 - Jogo da Adivinhação v.1.0#
import random  
import time
print(" estou pensando em uma numero de 0 a 5, consegue adivinhar?")
jogo=[0,1,2,3,4,5]
sorteio=random.choice(jogo)
#print(" {}".format(sorteio))
numero=int(input("qual o numero que eu pensei "))
print("Processando.....")
time.sleep(3)
if numero == sorteio:
    print("parabens, voce acertou!")
else:
    print("errrroooooouuuuuuuuuuu!!!!!")
