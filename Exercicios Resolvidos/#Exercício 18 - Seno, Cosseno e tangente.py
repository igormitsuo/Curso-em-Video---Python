#Exercício Python #018 - Seno, Cosseno e Tangente#
import math
x=float(input("digite o angulo que voce deseja"))
print("o seno do angulo é {:.2f}.".format(math.sin(math.radians(x))))
print("o cosseno do angulo é {:.2f}.".format(math.cos(math.radians(x))))
print("a tangente do angulo é {:.2f}.".format(math.tan(math.radians(x))))