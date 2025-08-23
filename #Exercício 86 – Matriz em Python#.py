#Exercício 86 – Matriz em Python#
#modo formça bruta
'''matx=([],[],[])
for c in range (0,3):
    num=int(input(f"Digite um numero para posição [0,{c}]\n"))
    matx[0].append(num)
for c in range (0,3):
    num=int(input(f"Digite um numero para posição [1,{c}]\n"))
    matx[1].append(num)
for c in range (0,3):
    num=int(input(f"Digite um numero para posição [2,{c}]\n"))
    matx[2].append(num)
print (f"[{matx[0][0]}] [{matx[0][1]}] [{matx[0][2]}]\n[{matx[1][0]}] [{matx[1][1]}] [{matx[1][2]}]\n[{matx[2][0]}] [{matx[2][1]}] [{matx[2][2]}]")'''
#modo inteligente guanabara

matx=[[0,0,0],[0,0,0],[0,0,0]]     
for l in range (0,3):
    for c in range (0,3):
        matx[l][c] = int(input(f"digite um valor par [{l},{c}]: "))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f"[{matx[l][c]:^5}]",end=" ")
    print()
