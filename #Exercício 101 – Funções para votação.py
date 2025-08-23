#Exercício 101 – Funções para votação
from datetime import date
def voto(ano_nasci):    
    ano_atual=date.today().year
    idade= (ano_atual-ano_nasci)
    #print(idade)
    if idade<18:
        return f'Sua idade é {idade}, seu voto é negado'
    elif idade>=18 and idade <=60:
       # return (f"Sua idade é {idade}, seu voto é obrigatorio")
        print(f'Sua idade é {idade}, seu voto é obrigatorio') 
    else: 
        idade >60                     
        return (f"Sua idade é {idade}, seu voto é opcional"   )

ano_nasci=int(input("Entre com seu ano de anscimento \n"))
voto(ano_nasci)
#print(voto(ano_nasci))