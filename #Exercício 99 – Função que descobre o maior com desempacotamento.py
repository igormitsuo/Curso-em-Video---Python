#Exercício 99 – Função que descobre o maior -desempacotamento
from time import sleep

def maior(*numeros):
    contagem=0
    maior=0
    print("-="*20)
    print("Analizando valores passados .....")
    for valor in numeros:
        print(f'{valor}',end=" ",flush=True)
        sleep(0.3)
        if contagem ==0:
            maior= valor
        else:
            if valor> maior:
             maior = valor
        contagem +=1
    print(f'Foram informador {contagem} valores ao todo')
    print(f'o maior valor informado foi {maior}')

maior(2,5,1,9,7,4)
maior(1,9,15,21,-5)
maior(-1,-4,-2,-17)
maior()