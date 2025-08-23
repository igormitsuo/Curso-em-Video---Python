#Exercício 94 – Unindo dicionários e listas#
cad={}
lista_geral=[]
cont_sex=0
cont_pessoas=0
cont_idade=0
media_idade=0

while True:
    cad.clear()
    cad['nome']=str(input("Entre com o nome \n"))
    cad['idade']=int(input("Entre com a idade \n"))
    cad['sexo']=str(input("Entre com o sexo M\F\n")).upper()  
    lista_geral.append(cad.copy())
    print(cad)
    print(lista_geral)
    cont_pessoas+=1
    cont_idade +=cad["idade"]
    media_idade=cont_idade/cont_pessoas
    resp=str(input("quer continuar ? [s/n]\n"))
    if resp in"Nn":
        break
print(lista_geral)  
print(f"Foi cadastrado {cont_pessoas} pessoas")
print(f"A media de idade cadastrada é de {media_idade} ")
print(f'As mulheres cadastradas foram ', end= " ")
for p in lista_geral:
    if p["sexo"] in "fF":
        print(f'{p["nome"]}', end= " ")
print(" ")
print(f'Pessoas com idade acima da media: ')
for p in lista_geral:
    if p["idade"]>= media_idade:
        print(" ")
        for k,v in p.items():
            print(f'{k} = {v}; ' ,end= " ")
print(" ") 
print("Encerrado")

#copia de lista = lista[:]
#apagar lista = lista.clear ()