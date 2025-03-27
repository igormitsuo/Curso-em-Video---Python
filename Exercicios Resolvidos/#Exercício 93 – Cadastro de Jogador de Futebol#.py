#Exercício 93 – Cadastro de Jogador de Futebol#
geren={}
gols=[]
gol=0
geren['nome']= str(input(f"Nome do jogador\n"))
geren['total_part']= int(input(f"Quantas partidas jogou\n"))
for i in range(0,geren['total_part']):
    gol=int(input(f" Qauntos gols marcou no {i+1}º jogo "))
    gols.append(gol)
geren['gols']=gols
geren['total_gols']=sum(gols)
print(geren)
print(gols)
print('-='*30)
for k,v in geren.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jofador {geren["nome"]}, jogou {geren["total_part"]} partidas')
for v in range (0,geren['total_part']):
    print(f'Na partida {v+1},fez {gols[v]} gols ')
print(f'Foi um total de {geren["total_gols"]} gols')

