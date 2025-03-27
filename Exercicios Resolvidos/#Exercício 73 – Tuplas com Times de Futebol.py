#Exercício 73 – Tuplas com Times de Futebol#
colocação=("botafogo","palmeiras",'flamengo','fortaleza','são paulo',
           'bahia','cruzeiro','atleticoPR','rb_bragantino','atleticoMG',
           'vasco','juventude','internacional','curintia','criciuma',
           'vitoria','cuiaba','gremio','fluminence','atleticoGO')
print("*-"*20)
print(f"os cinco primeiros times do campeonato são :\n{colocação[0:5]}")
print("*-"*20)
print(f"os ultimos quatro colocados são:\n{colocação[-4:]}")
print("*-"*20)
#funciona dos dois modos
#ordemcolocação=sorted(colocação)
#print(f"Os Times em ordem alfabética:\n{ordemcolocação}")
print(f"Os Times em ordem alfabética:{sorted(colocação)}")
print("*-"*20)
procuratime=str(input("procure a classificação do seu time no tabela\n ")).strip()
print(f"a colocação do seu time é:\n {colocação.index(procuratime)+1}º colocado")