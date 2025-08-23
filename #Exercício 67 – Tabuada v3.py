#Exercício 67 – Tabuada v3.0#
while True:
    tab=result=0
    num=int(input(f"tabuada de qual numero voce deseja ? "))
    if num<0:
        break
    #pode usar o for c in range (1,11):
    while tab!=11:
        result=num*tab
        print(f"{num} x {tab} = {result}")
        tab+=1
print(f"terminou")
