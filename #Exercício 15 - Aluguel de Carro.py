#Exercício Python #015 - Aluguel de Carros#
dias=int(input("por quantos dias o carro foi alugado?"))
km=float(input("quantos KM foram percorridos"))
custo= dias*60 +(km*0.15)
print("o carro foi alugado por {} dias e percorrido {} km, dando um total a pagar de {:.2f}".format(dias,km,custo))