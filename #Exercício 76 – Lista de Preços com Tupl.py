#Exercício 76 – Lista de Preços com Tupla#
'''resolução igor:
print("--"*20)
print(f'{"LISTA DE PREÇOS":^40}')
print("--"*20)
list=("lapis","borracha","caderno","estojo","transferidor","cpmpasso","mochila","canetas","livros",
      "1.75","2.00","15.90","25.00","4.20","9.99","120.00","22.30","34.90",)
print(f'{list[0]:<}{"."*50} R$   {list[9]:>}\n{list[1]:<}{"."*47} R$   {list[10]:>}\n{list[2]:<}{"."*48} R$  {list[11]:>}\n{list[3]:<}{"."*49} R$  {list[12]:>}\n{list[4]:<}{"."*43} R$   {list[13]:>}\n{list[5]:<}{"."*47} R$   {list[14]:>}\n{list[6]:<}{"."*48} R$ {list[15]:>}\n{list[7]:<}{"."*48} R$  {list[16]:>}\n{list[8]:<}{"."*49} R$  {list[17]:>}')'''
#resolução guanabara#
listagem=("lapis","1.75","borracha","2.00","caderno",
          "15.90","estojo","25.00","transferidor","4.20",
          "cpmpasso","9.99","mochila","120.00","canetas",
          "22.30","livros","34.90")
print("--"*20)
print(f'{"LISTA DE PREÇOS":^40}')
print("--"*20)
for pos in range (0,len(listagem)):
    if pos %2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7}')
print("--"*20)         