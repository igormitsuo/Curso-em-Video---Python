#Exercício 90 – Dicionário em Python
   
aluno={}
cadastro=[]
media=0
sit=0
while True:
    aluno["nome"]=str(input("Entre com o nome do aluno\n"))
    aluno["media"]=float(input("Entre com a media do aluno\n"))
 
    if aluno["media"]>=7:
        aluno["situação"]="aprovado"
        print("aprovado")
    elif 5<= aluno["media"]<7:
        aluno["situação"]="recuperação"
        print("recuperação")
    if aluno["media"]<5:
        aluno["situação"]="reprovado"
        print("reprovado")
    cadastro.append(aluno.copy())   
    opc=str(input("Deseja continuar?\n")).upper().strip()
    #funciona desse jeito 
    '''print(f"- O nome do aluno é {aluno['nome']}")
    print(f"- A média do aluno é {aluno['media']}")
    print(f"- A situação atual dele é {aluno['situação']}")'''
    if opc== "N":
        break
#funciona tambem deste jeito  
for k,v in aluno.items():
    print(f'{k} é igual á {v}')
