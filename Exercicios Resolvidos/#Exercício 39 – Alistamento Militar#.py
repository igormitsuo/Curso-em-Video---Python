#Exercício 39 – Alistamento Militar#
from datetime import date
data=date.today().year
ano_nascimento=int(input(" Entre com seu ano de nascimento "))
alistamento= data-ano_nascimento
print(" Voce tem {} anos".format(alistamento))
if alistamento<18:
    print(" Faltam {} anos, e voce não precisa se alistar agora, só em {}".format(18-alistamento,(18-alistamento)+data))
elif alistamento>18:
    print(" Passou {} anos do seu alistamento e seu alistamento foi em {}".format(alistamento-18,(alistamento-18)-data))
else:
    print(" Esse é o ano do seu alistamento")
