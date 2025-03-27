#Exercício 102 – Função para Fatorial

'''from math import factorial
def fatorial(num,show):
    if show==True:
        cont=num
        while cont!=0: 
            fat=factorial(num)   
            print(f'{cont} x ',end=" ")
            cont-=1
        print (f' = {fat}') 
    else:
        print(f" O fatorial de {num} é {factorial(num) }")
        #print(f'{factorial(num) }')
#return f'{fat}'
fatorial(5,show=False)
#print(fatorial(5,False))'''
from math import factorial
def fatorial(num,show=False):
    
    '''calcular fatorial de um numero
    num -> numero a ser calculado
    show-> parametro opcional
    factorial -> função matematica para realizar fatoração de um numero
    return -> retorna o valor do numero fatorado'''

    if show==True:
        cont=num
        while cont!=0: 
            fat=factorial(num)
            print(f'{cont}',end=" ")  
            if cont>1:   
                print(' x ',end=" ")
                cont-=1
            else:
                print(f' = ',end=" ")
                cont-=1
        print(f'{fat} ')
        return("")   
    else:
        return (f" O fatorial de {num} é {factorial(num) }")
        

print(fatorial(10,show=True))
help(fatorial)


