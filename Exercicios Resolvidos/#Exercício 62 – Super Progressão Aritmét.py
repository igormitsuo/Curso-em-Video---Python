#Exercício 62 – Super Progressão Aritmética v3.0- feito pelo guanabara#
print(" gerador de PA")
print("-="*30)
primeiro=int(input(" entre com o primeiro termo da PA: "))
razão=int(input("entre com a razão da PA: "))
termo=primeiro
cont=1
total=0
mais =10
while mais!=0:
    total=total+mais
    while cont<=total:
        print("{}-> ".format(termo),end="")
        termo +=razão
        cont+=1
    print("pausa")
    mais=int(input("quantos termos a mais voce deseja mostrar? "))
print("progressão finalizada com {} termos mostrados".format(total))