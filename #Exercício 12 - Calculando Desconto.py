#Exercício Python #012 - Calculando Descontos#
produto= float(input("qual o valor do produto em R$"))
porcentagem= float(input(" entre com o valor do desconto em %"))
desconto = produto - (produto*(porcentagem/100))
print("o valor do produto que custava {}, na promoção com {} %""de desconto vai custar R$ {:.2f} ".format(produto,porcentagem,desconto))
