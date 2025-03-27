#Exercício 96 – Função que calcula área
def area(L,C):
    A=L*C
    print(f'O terreno de {L} de largura, {C} de comprimento tem {A} de área')
L=float(input("Entre com a largura do terreno \n"))
C=float(input("Entre com o comprimento do terreno \n"))
area(L,C)

