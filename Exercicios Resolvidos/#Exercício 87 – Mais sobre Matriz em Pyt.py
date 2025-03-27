#Exercício 87 – Mais sobre Matriz em Python#
soma=0
coluna3=0
linha2=[]
matx=[[0,0,0],[0,0,0],[0,0,0]]     
for l in range (0,3):
    for c in range (0,3):
        matx[l][c] = int(input(f"digite um valor par [{l},{c}]: "))
        if matx[l][c] %2==0:
            soma+= matx[l][c]
linha2.append(matx[1][0])  
linha2.append(matx[1][1])
linha2.append(matx[1][2])        
coluna3= matx[0][2]+matx[1][2] +matx[2][2] 
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f"[{matx[l][c]:^5}]",end=" ")
    print()
print(f"A soma dos valores pares é {soma}")
print(f"A soma dos valores da 3º coluna é {coluna3}")
#print(linha2)
print(f"O maior valor da 2º linha é {max(linha2)}" )



