#Exercício 106 – Interactive helping system in Python
def função ():
    while True:
        func=str(input("FUNÇÃO OU BIBLIOTEC > "))
        if func != "fim":
            help(func)
        else:
            print("ATÉ LOGO")
            break       



print("-="*20)
print("SISTEMA DE AJUDA  PyHELP")
print("-="*20)
função()

