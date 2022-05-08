valor = float(input('Qual o valor do produto? R$: '))
dinheiro = valor * 0.9
cartão = valor * 0.95
cartão3x = valor * 1.2

pagamento = int(input('Forma de pagamento:\n[1] Dinheiro\n[2] A vista no cartão\n[3] Cartão em até 2x\n[4] Cartão 3x ou mais\nDigite aqui: '))

if pagamento == 1:
    print('O valor final ficou em R$: {:.2f}.'.format(dinheiro))
elif pagamento == 2:
    print('O valor final ficou em R$: {:.2f}.'.format(cartão))
elif pagamento == 3:
    print('O valor final ficou em R$: {:.2f}.'.format(valor))
elif pagamento == 4:
    parcelas = int(input('Em quantas vezes quer parcelar? '))
    print('Sua compra de R$: {:.2f} ficou com o valor total de R$: {:.2f}.'.format(valor, cartão3x))
    print('O valor das parcelas ficou em R$: {:.2f}.'.format(cartão3x/parcelas))
else:
    print('Forma de pagamento digitado incorreto.')
