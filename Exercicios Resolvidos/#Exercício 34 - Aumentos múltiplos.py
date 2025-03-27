#Exercício Python #034 - Aumentos múltiplos#
salario=(float(input("digite o salario do colaborador R$  ")))
if salario>= 1250.00:
    salario=(salario*0.10)+salario
    print(" o almento do salario foi de R$ {:.2f}".format(salario))
else:
    salario=(salario*0.15)+salario
    print(" o almento do salario foi de R$ {:.2f}".format(salario))