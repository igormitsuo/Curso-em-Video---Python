#Exercício 91 – Jogo de Dados em Python- resolução guanabara #
from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador_01':randint(1,6),'jogador_02':randint(1,6),'jogador_03':randint(1,6),'jogador_04':randint(1,6)}
ranking=list()
print("valores sorteados: ")
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado ')
    sleep(1)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-='*30)
print('==' 'RANKING DOS JOGADORES' '==')
for i,v in enumerate(ranking):
    print(f'{i+1}º luga: {v[0]} com {v[1]} ')
    sleep(1)
