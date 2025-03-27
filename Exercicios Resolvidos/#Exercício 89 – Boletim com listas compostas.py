#Exercício 89 – Boletim com listas compostas
'''lista1=[]
temp=[]
medias=[]
n=0
ind=0
while n!=2:
    x=int(input("entre com um numero\n"))
    y=str(input("entre com um nome\n"))
    z=float(input("entre com uma nota\n"))
    n+=1
    temp.append(x)
    temp.append(y)
    temp.append(z)
    lista1.append(temp[:])
    print(temp)
    temp.clear()
#print(lista1)
for i,l in enumerate(lista1):
    #print(f"{i+1}:{l}")
    #print(f"{i+1}     {l[0]}   {l[1]}   {l[2]}")
    print(f"{l[2]}",end=" ")
print'''

lista1=[]
temp=[]
tempmedia=[]
medias=[]
n=0
ind=0
media=0
opção2=0

while True:
    y=str(input("Entre com um nome\n"))
    x=float(input("Entre com a 1º nota\n"))    
    z=float(input("Entre com a 2º nota\n"))
    media= (x+z)/2
    temp.append(y)
    temp.append(x)
    temp.append(z)
    tempmedia.append(y)
    tempmedia.append(media)
    lista1.append(temp[:])
    medias.append(tempmedia[:])
    temp.clear()
    tempmedia.clear()
    opção=str(input("Deseja continuar? S/N\n ")).strip().upper()
    if opção=="N":
        break
print(f'{"Ind"} {"Nome":>10} {"media":>8}')
print('-'*40)
for i,l in enumerate(medias):
   print(f"{i+1}  {l[0]:>10}  {l[1]:>8.1f} ")
    #print(f"{i+1}      {l[0]}       {l[1]}         {l[2]}")
#print(lista1)
#print(medias)
#print(lista1[0][0])
while True:
    opção2=int(input("Mostrar notas de qual aluno?(999 interrompe)\n ")) 
    if opção2 == 999:
     print("FINALIZANDO")
     break   
    #if opção2<= len(lista1):
    else:
        print(f'As notas de {lista1[opção2-1][0]} foram {lista1[opção2-1][1]} e {lista1[opção2-1][2]}')
print("obrigado")