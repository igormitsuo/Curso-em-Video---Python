#Exercício 66 – Vários números com flag#
cont=soma=0
while  True:
    num=int(input("entre com um numero. caso queira para digite 999 "))
    if num==999:
        break
    cont+=1
    soma+=num    
print(f"foram digitados {cont} e a soma entre eles é de {soma}")

