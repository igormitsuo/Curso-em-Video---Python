#Exercício 60 – Cálculo do Fatorial#
import math 
n=int(input(" entre com um numero para calcular o fatorial "))
c=n
f=1
'''while 
    result= math.factorial(n)
    print("o fatorio de  {} é ".format(result))
print("fim")'''
print(" calculando o fatorial de {}! =".format(n),end=" ")
while c> 0:
    print("{}".format(c),end=" ")
    print("x" if c>1 else "=",end=" ")
    f*=c
    c-=1
print("{}".format(f))



