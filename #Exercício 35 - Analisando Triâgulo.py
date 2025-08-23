#Exercício Python #035 - Analisando Triângulo v1.0#
r1=float(input("entre com o valor da primeira reta "))
r2=float(input("entre com o valor da segunda reta "))
r3=float(input("entre com o valor da terceira reta "))
if (r1+r2)>r3 and (r3+r1)>r2 and (r3+r2)>r1:
    print("as retas {:.2f}, {:.2f} e {:.2f} formam um triangulo".format(r1,r2,r3))
else:
    print("as retas {:.2f}, {:.2f} e {:.2f} não formam um triangulo".format(r1,r2,r3))