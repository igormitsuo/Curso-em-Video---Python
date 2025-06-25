#Relatorio diario- Excel com Python

from openpyxl import Workbook 
from openpyxl import load_workbook
from time import sleep
from datetime import datetime



def menu():
 print('''
********** RELATORIO DIARIO DE ATIVIDADES **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] CRIAR NOVO RELATORIO

**************************************
''')
 
 valor=int(input("Entre com a opção \n"))
 if valor not in [0,1]:
  print("## OPÇÃO INVALIDA: DIGITE UM VALIDO##")
  sleep(2)
 return(valor)

def criar_relatorio():
  arquivo=Workbook()
  nome_do_arquivo=str(input("Digite o nome do aquivo\n"))
  nome_do_arquivo=nome_do_arquivo.strip()+".xlsx"  
  aba=arquivo.active
  aba.title="MODELO"
  print(f"Arquivo '{nome_do_arquivo}' criado com sucesso.")
  modelo=arquivo["MODELO"]
  modelo.append(["ITEM:","EQUIPAMENTO:","ÁREA:","DATA","HORA DE INICIO","HORA FIM","TOTAL","DESCRIÇÃO DA ATIVIDADE:","EXECUTANTES:","STATUS"])  
  arquivo.save(f'{nome_do_arquivo}')
 

  
while True:   
 opção=menu()
 if opção==0:
  print("OPÇÃO SAIR")
  sleep(2)
  break  
 elif opção==1:
  criar_relatorio()
 
  


 