#Exercício Python #029 - Radar eletrônico#
velo=int(input("qual a velocidade atual do carro  "))
if velo>80:
    limite=(velo-80)
    multa=limite*7
    print("\033[31m voce ultrapassou o limite de velocidade em {} Km/h e foi multado em R$ {:.2f}\033[m".format(limite,multa))
else:
    print("sua velocidade de {} Km/h, está dentro do limite, boa viagem".format(velo))
