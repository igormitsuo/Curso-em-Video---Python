#Exercício 71 – Simulador de Caixa Eletrônico#
cont50=0
cont20=0
cont10=0
cont01=0
while True:
    valor=int(input("digite o valor que deseja sacar R$ \n"))
    vt=valor
    while valor>=50:
        valor-=50
        cont50+=1
    while valor>=20:
        valor-=20
        cont20+=1
    while valor>=10:
        valor-=10
        cont10+=1
    while valor>=1:
        valor-=1
        cont01+=1
    if valor<=0:
        break
print(f"o valor solicitado foi de R$ \n{vt :.2f} \nforam necessarias:\n{cont50} notas de 50 Reais \n{cont20} notas de 20 Reais \n{cont10} notas de 10 Reais \n{cont01} notas de 1 Real \n")




