print('Para avaliarmos se você poderá financiar a casa, preencha os dados abaixo: ')
vcasa = float(input('Valor da casa R$: '))
salario = float(input('Salário R$: '))
tempo = int(input('Quantos anos para pagar: '))
prest = (vcasa / tempo) / 12
neg = salario * 0.3

if prest > neg:
    print('O valor da prestação está maior do que 30% do seu salário, devido a isso o financiamento foi negado.')
    print('Valor da prestação: R$: {:.2f}.'.format(prest))
    print('Para que seja aprovado a prestação deve ser até o maximo de R$: {:.2f}.'.format(salario * 0.3))
else:
    print('O financiamento foi aprovado.')
    print('A prestação será de R$: {:.2f} por mês.'.format(prest))