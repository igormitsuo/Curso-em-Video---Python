
#Exercício 95 – Cadastro de Jogador de Futebol Melhorado# não concluido
jogador={}
gols=[]
lista_de_jogadores=[]
cod=1
while True:
    #gols.clear()  
    jogador['cod_jogador']=cod
    jogador['nome']=str(input("Entre com o nome do jogador "))
    jogador['quant_partidas']=int(input("Quantidade de partidas jogadas "))
    for g in range (0,jogador['quant_partidas']):  
        gol=0            
        gol=int(input(f"Entre com os gols na {g+1}º partida "))
        gols.append(gol)
        jogador['gols']=gols 
    jogador['total de gols']= sum(gols)
    print(f"Total de gols na partida:{jogador['total de gols']} ")
    lista_de_jogadores.append(jogador.copy()) 
    print(jogador)
    print(lista_de_jogadores)
    gols.clear()  
    resp=str(input("Deseja continuar? S/N ")).upper()
    cod+=1
    jogador.clear()
    if resp in "nN":
        break
print("-="*20)
print('cod_jodador',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
print("-="*20)
for k,v in enumerate(lista_de_jogadores):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print("-="*20)


