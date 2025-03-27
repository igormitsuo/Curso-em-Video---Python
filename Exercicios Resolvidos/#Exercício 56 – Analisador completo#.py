#Exercício 56 – Analisador completo#
somaidade=0
mediaidade=0
maioridadedehomem=0
nomevelho=0
totmulher20=0
for p in range (1,5):
    print(" -------{}º pessoa --------- ".format(p))
    nome =str(input("nome: ")).strip()
    idade=int(input("idade "))
    sexo=str(input("sexo [M / F]: ")).strip()
    somaidade+=idade
    if p ==1 and sexo in "Mm":
        maioridadedehomem=idade
        nomevelho= nome
    if sexo in "Mm"and idade> maioridadedehomem:
        maioridadedehomem=idade
        nomevelho=nome
    if sexo in "Ff" and idade <20:
        totmulher20+=1
        mediaidade=somaidade/4
print("a media do grupo é de {} anos".format(mediaidade))
print("o homem mais velho tem {} anos, e se chama {}".format(maioridadedehomem,nomevelho))
print("ao todo são {} mulheres com menos de 20 anos".format(totmulher20))

'''for d in range (1,5):
    print("{} pessoa".format(d))
    if d==1:
        nome1=str(input("nome: "))
        idade1=int(input("idade "))
        sexo1=str(input("M /F "))
    if  d==2:
        nome2=str(input("nome: "))
        idade2=int(input("idade "))
        sexo2=str(input("M /F "))
    if  d==3:
        nome3=str(input("nome: "))
        idade3=int(input("idade "))
        sexo3=str(input("M /F "))
    if  d==4:
        nome4=str(input("nome: "))
        idade4=int(input("idade "))
        sexo4=str(input("M /F "))
media=(idade1+idade2+idade3+idade4)/4
print("a media de idade das pessoas é {}".format(media))'''



