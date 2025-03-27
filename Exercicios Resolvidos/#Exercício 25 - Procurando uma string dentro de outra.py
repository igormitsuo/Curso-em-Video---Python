#Exercício Python #025 - Procurando uma string dentro de outra#
nome=str(input("digite seu nome completo ")).strip()
print(" seu nome tem silva ?{} ".format('silva' in nome.lower()))