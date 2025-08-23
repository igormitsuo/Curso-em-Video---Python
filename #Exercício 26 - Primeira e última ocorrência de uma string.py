#Exercício Python #026 - Primeira e última ocorrência de uma string#
frase=str(input("digite uma frase \n")).lower()
frase.strip()
print("a letra A, aparece {} vezesz".format (frase.count("a")))
print("a primeira letra A, aparece na posição {}".format (frase.find("a")))
print("a ultima letra A,apareceu na posição {}".format (frase.rfind("a")))