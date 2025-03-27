#Exercício 83 – Validando expressões matemáticas3#
#resolução guanabara
exp=str(input("digite a expressão: "))
pilha=[]
for simb in exp:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('sua expressão está valida')
else:
    print("sua expressão esta errada")
