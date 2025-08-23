#Exercício Python #022 - Analisador de Textos#
nome=str(input("digite seu nome completo ")).strip()
print("analisando seu nome .... ")
print("seu nome em maiusculo é {}".format(str.upper(nome)))
print("seu nome em minusculo é {}".format(str.lower(nome)))
print("seu nome tem ao todo {}".format(len(nome)-nome.count(" ")))
#print("seu primeiro nome é {} e tem {} letras".format(nome,nome.find(' ')))
separa=nome.split()
print("seu primeiro nome é {}, e tem {} letras".format(separa[0],len(separa[0])))
