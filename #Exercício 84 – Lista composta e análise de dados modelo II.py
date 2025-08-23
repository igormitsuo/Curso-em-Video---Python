#Exercício 84 – Lista composta e análise de dados Modelo 02#
temp=[]
princ=[]
mai=men=0
while True:
    temp.append(str(input("nome\n")))
    temp.append(float(input("peso\n")))
    if len(princ)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input("quer continuar ? [s/n]\n"))
    if resp in"Nn":
        break
print('-='*30)
print(f'ao todo voce cadastrou {len(princ)} pessoas. ')
print(f'o maior peso digitado foi de {mai} kg. peso de ',end=" ")
for p in princ:
    if p[1]==mai:
        print(f'{p[0]}',end= " ")
print()
print(f'o menor peso foi de {men}kg peso de ',end=" ")
for p in princ:
    if p[1]==men:
        print(f'{p[0]} ',end=" ")
print()
