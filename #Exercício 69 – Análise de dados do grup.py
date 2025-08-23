#Exercício 69 – Análise de dados do grupo#
cont=0
contamulher=0
contahomem=0
while True:
    idade=int(input("digite sua idade\n"))
    if idade<18:
        cont+=1
    sexo=str(input("digite seu sexo \n")).strip().upper()[0]
    while sexo not in "MF":
        sexo=str(input("digite seu sexo \n")).strip().upper()[0]
    if idade<20 and sexo=="F":
        contamulher+=1
    if sexo=="M":
        contahomem+=1
    escolha=str(input("deseja continuar S/N \n")).strip().upper()[0]
    while escolha not in "SN":
         escolha=str(input("deseja continuar S/N \n")).strip().upper()[0]
    if escolha in "N":
     break
print(f"foram cadastradas {cont} pessoas com menos de 18 anos")
print(f"foram cadastrados {contahomem} homens")
print(f"foram cadastrados {contamulher} mulheres com menos de 20 anos")