#Exercício 99 – Função que descobre o maior
lista= []
cont=0
opc="s"
#função
def maior(lista):
    print('-='*20)    
    print("Analiszando os valores informador....")
    for n in lista:
        print(f'{n} ', end="" )
    #print(" ")
    print(f'...foram informados {cont} numeros ao todo')
    print(f"o maior valor é {max(lista)}")
#principal
while True:
    num=int(input("Entre com um numero \n"))
    lista.append(num)    
    opção=str(input("Deseja continuar? S/N\n ")).strip().upper()
    if len(lista)>0:
        cont+=1
    if opção=="N":
        break
maior(lista)


