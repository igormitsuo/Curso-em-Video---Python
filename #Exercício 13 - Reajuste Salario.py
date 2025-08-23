#Exercício Python #013 - Reajuste Salarial#
salario=float(input("qual o salario do funcionario?"))
porcentagem=float( input("qual a %"" de almento"))
aumento= salario +(salario * (porcentagem/100))
print("um funcionario que ganhava R$ {}, com {} % de aumento, passa a receber R$ {:.2f} ".format(salario, porcentagem, aumento))