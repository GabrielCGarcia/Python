n = float(input('Conversor de moeda, real para dolar, euro e dolar canadense: R$:'))
dol = n / 5.09
eur = n / 5.35
cad = n / 3.96
print('Seu valor de R$: {:.2f} convertido em dolar é US$:{:.2f}, em euro é €$:{:.2f} e em dolar canadense é C$:{:.2f}.'.format(n,dol,eur,cad))