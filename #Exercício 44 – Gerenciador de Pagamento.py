#Exercício 44 – Gerenciador de Pagamentos#
#print("{:=^40}".format(" lojas guana bara "))
print("="*15,"LOJAS GUANABARA","="*15)
compra=float(input("valor total das compras R$  "))
print(" FORMAS DE PAGAMENTO")
print(" [ 1 ] A VISTA DINHEIRO/CHEQUE\n [ 2 ] A VISTA NO CARTÃO\n [ 3 ] 2X CARTÃO\n [ 4 ] 3X OU MAIS NO CARÃO  ")
op=int(input(" qual a sua opção "))
if op==1:
   desconto= compra - (compra*0.10)
   print("sua compra de R$ {:.2f},com 10%""de desconto, vai custar R$ {:.2f} ".format(compra,desconto))
elif op==2:
   desconto= compra -(compra*0.05)
   print("sua compra de R$ {:.2f},com 05%" "de desconto, vai custar R$ {:.2f} ".format(compra,desconto))
elif op==3:
   print("sua compra de R$ {:.2f} , em 2x no cartão, fica 2 parcelas de R$ {:.2f} ".format(compra, compra/2))
elif op==4:
    parceleas=int(input("em quantas parcelas "))
    if parceleas >=3:
        print("sua compra de R$ {:.2f} parcelada em {} de {:.2f}, fica R${:.2f} com juros".format(compra,parceleas,(compra/parceleas),(compra +(compra*0.20))))
    else:
        print("")
else:print("opção invalida, comece de novo")

   
