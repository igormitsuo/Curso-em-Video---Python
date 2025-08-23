#Exercício 104 – Validando entrada de dados em Python
def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31m ERRO !. digite um valor inteiro valido !\033[m')
        if ok:
            break
    return n
    
  
n=leiaint("digite um numero: \n ")
print(f'Voce digitou o numero {n} ')