#Exercício 37 – Conversor de Bases Numéricas#
num=int(input(" Entre com o numero que deseja mudar de base  "))
base=int(input(" Escolha 1 para base binaria, Escolha 2 para base octal, Escolha 3 para base hexadecimal "))
if base==1:
    print("a opçãoescolida foi {}, e o valor do numero {} em binario é {}".format(base,num,(bin(num)[2:])))
elif base==2:
    print("a opçãoescolida foi {}, e o valor do numero {} em binario é {}".format(base,num,(oct(num)[2:])))
elif base==3:
    print("a opçãoescolida foi {}, e o valor do numero {} em binario é {}".format(base,num,(hex(num)[2:])))
else:
    print(" opção invalida, tente novamente")