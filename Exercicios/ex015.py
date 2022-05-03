Cdia = float(input('Quantos dias alugados? '))
Ckm = float(input('Quantos km rodados? '))
Ctotal = (Cdia * 60) + (Ckm * 0.15)
print('O valor a pagar por {:.0f} dias e {:.0f}km rodados é de: R$:{:.2f}'.format(Cdia,Ckm,Ctotal))