#Exercício Python #017 - Catetos e Hipotenusa#
from math import hypot
x=float(input("entre com o comprimento do cateto oposto"))
y=float(input("entre com o comprimento do cateto adjacente"))
print("o valor do cateto oposto é {}, o valor do cateto adjacente é {}, e o valor da hipotenusa é {:.2f}".format(x,y,hypot(x,y)))