#Exercício 98 – Função de Contador v guanabara#
from time import sleep
#função
def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print('-='*20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont=1
        while cont<=f:
            print(f"{cont}",end=" ",flush=True)
            sleep(0.3)
            cont+=p
        print("fim")
    else:
        cont=i
        while cont>=f:
            print(f"{cont}",end=" ",flush=True)
            sleep(0.3)
            cont-=p
        print("fim")

contador(1,10,1)
contador(10,0,2)
print('-='*20)
print("Agora é sua vez de personalizar a contagem")
inicio=int(input("Entre com o inicio da contagem\n"))
fim=int(input("Entre com o final da contagem\n"))
passo=int(input("Entre com o passo\n"))
contador(inicio,fim,passo)