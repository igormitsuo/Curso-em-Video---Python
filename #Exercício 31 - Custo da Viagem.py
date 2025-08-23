#Exercício Python #031 - Custo da Viagem#
dist=float(input("qual a distancia da viagem em KM ?  "))
if dist>200:
    #passagem=dist*0.5
    print("o valor da passagem é de R$ {:.2f}".format(dist*0.5))
else:
    #passagem=dist*0.45
    print("o valor da passagem é de R$ {:.2f}".format(dist*0.5))
    