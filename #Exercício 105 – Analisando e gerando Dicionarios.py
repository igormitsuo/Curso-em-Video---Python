#Exercício 105 – Analisando e gerando Dicionários
def notas(*n,sit=False):
   """
   função para anlisar nostas e situação de varios alunos
   paran. n:->uma ou mais nostas dos alunos(*aceita varias)
   paran. sit:->valor opcional, indica se deve ou não mostrar a situação
   paran. return:-> dicionario com a situação da turma
   """
   r=dict()
   r['total']= len(n)
   r['maior']= max(n)
   r['menor']= min(n)
   r['média']= sum(n)/len(n)
   if sit:
      if r["média"] >=7:
        r["siturção"]= "Boa"
      elif r["média"] >5:
        r["siturção"]= "RAZOAVEL"
      else:
       r["siturção"]= "RUIM"
   return r
    
resp=notas(5.5, 2.5, 1.5,sit=True)
print(resp)
#help(notas)