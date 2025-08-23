#Exercício 103 – Ficha do Jogador

def ficha(jogador= '<desconhecido>' ,gol=0):
    print(f'o jogador {jogador} fez {gol} gol(s)no campeonato')
    '''if jogador== "desconhecido" and gol==0:
        print( f'O Jogador {jogador} fez {gol} gol(s) no campeonato')
    elif jogador== "desconhecido" and gols!=0:
       print( f'O Jogador {jogador} fez {gol} gol(s) no campeonato'     )
    else:
        print('O Jogador {jogador} fez {gol} gol(s) no campeonato')'''
    
print("-="*20)
nome =str(input("Entre com o nome do jogador \n"))
gols=str(input("Entre quantidade de gols no campeonato \n"))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=="":    
    ficha(gol=gols)
else:
    ficha(nome,gols)
print("-="*20)

