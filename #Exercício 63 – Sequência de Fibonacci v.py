#Exercício 63 – Sequência de Fibonacci v1.0#
print(" sequencia de fibonacci")
print("-="*50)
termo=int(input(" entre com quantos termos voce quer mostrar: "))
a=0
b=1
cont=3
print("{}->{}".format(a,b), end="")
while cont<=termo:
    soma=a +b
    print("->{}".format(soma), end= "")   
    a=b
    b=soma
    cont+=1
print("->fim")


