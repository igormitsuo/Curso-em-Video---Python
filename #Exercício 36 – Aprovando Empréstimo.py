#Exercício Python #36 – Aprovando Empréstimo#
vcasa=float(input("Qual o valor da casa que deseja comprar?  "))
salario=float(input("Qual o seu salario R$   "))
tempo=int(input("Em quantos anos voce deseja pagar  "))
prestacao= vcasa/(tempo*12)
vprestacao=(salario*0.30)
if prestacao > vprestacao:
    print(" o valor da casa é de R$ {}, o seu salario é de R$ {}, o tempo de pagamento é de {} anos".format(vcasa,salario,tempo))
    print("seu imprestimo foi NEGADO. o valor da parcela de R$ {:.2f}, fica acima de 30%"  "do seu salario".format(prestacao))
else:
    print(" o valor da casa é de R$ {}, o seu salario é de R$ {}, o tempo de pagamento é de {} anos".format(vcasa,salario,tempo))
    print(" seu imprestimo foi APROVADO, o valor da prestação é de R$ {:.2f}, abaixo de 30%"  "do seu salario".format(prestacao))