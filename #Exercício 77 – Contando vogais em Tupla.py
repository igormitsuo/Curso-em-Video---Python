#Exercício 77 – Contando vogais em Tupla#
#resolução guanabara
palavras=("aprender","programar","linguagem","phyton","curso","gratis","estudar","praticar")
for p in palavras:
    print(f'\nna palavra {p}temos' , end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')