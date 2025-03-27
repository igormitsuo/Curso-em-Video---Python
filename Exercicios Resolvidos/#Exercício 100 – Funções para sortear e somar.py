#Exercício 100 – Funções para sortear e somar
from random import randint
from time import sleep

def sorteia(numeros):
    print("sorteando 5 numeros:",end='')    
    while len(numeros)<=4:
        numeros.append(randint(1,10))
    for n in numeros:            
        print(f'{n}',end=' ',flush=True)
        sleep(0.3)

def somaPar(numeros):
    soma=0
    for qnum in numeros :
        if qnum %2==0:
             soma+= qnum
    print(f'\nSomando os valores pares de {numeros},temos {soma}' )

numeros=[]
sorteia(numeros)
somaPar(numeros)
