#Exercício 98 – Função de Contador#
#função
def contador(inicio,fim,passo):
 print("de 1 até 10, de 1 em 1 \n")
 for n in range (1,11,1):
  print(f'{n}',end=" ")
 print(" ")
 print("de 10 até 0, de 2 em 2  \n")
 for n in range (10,-1,-2):
   print(f'{n}',end=" ")
 print(" ")
 print("contagem personalizada  \n")
 for n in range (inicio,fim+passo,passo):
   print(f'{n}',end=" ")
 print(" ")
#Principal
inicio=int(input("Entre com o inicio da contagem\n"))
fim=int(input("Entre com o final da contagem\n"))
passo=int(input("Entre com o passo\n"))
contador(inicio, fim, passo)