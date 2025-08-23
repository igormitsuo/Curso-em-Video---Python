#Exercício 74 – Maior e menor valores em Tupla#
from random import randint
num=(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))    
print(f"os valores sorteados foram {num}")
#funciona dos dois jeitos
#nov=sorted(num)
#print(nov)
#print(f"o maior valor da lista é {nov[4]} e o menor é {nov[0]}")
print(f"o maior valor da lista é {max(num)} e o menor é {min(num)}")