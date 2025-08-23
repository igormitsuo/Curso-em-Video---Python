#Exercício 57 – Validação de Dados#
sexo=str(input("entre com seu sexo [M /F] " )).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input("opção invalida, entre com o seu sexo: entre com seu sexo [M /F] " )).strip().upper()[0]
print("seu sexo é {}".format(sexo))
