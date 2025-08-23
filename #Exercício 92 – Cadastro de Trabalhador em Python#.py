#Exercício 92 – Cadastro de Trabalhador em Python#
from datetime import datetime
cad={}
cad["nome"]=str(input(f"Entre com o nome\n"))
cad["nascimento"]=datetime.now().year-int(input(f'Entre com o ano de nascimento formato /aaaa\n'))
CTPS=int(input(f'Entre com o numero da carteira de trabalho\n'))
if CTPS !=0:
    cad["CTPS"]=CTPS
    cad['contratação']=int(input(f'Entre com o ano de contratação formato /aaaa\n'))
    cad['salario']=float(input(f"entre com o valor da contratação R$ \n"))
    cad['aposentadora']= cad['nascimento']+((cad["contratação"]+35)-datetime.now().year)
    print('-='*30)
    print('==' 'CADASTRO' '==')
    print(f'Nome: {cad["nome"]}')
    print(f'Idade: {cad["nascimento"]}')
    print(f'CTPS: {cad["CTPS"]}')
    print(f'Ano de contratação: {cad["contratação"]}')
    print(f'valor de contratação: {cad["salario"]}')
    print(f'idade de aposentadoria: {cad["aposentadora"]}')
    print(cad)
print("fim")