print('\nResumo de Compras.\n')
total = mil = c = prodB = 0
prodBC = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço R$: '))
    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    total += preço
    c += 1
    if preço >= 1000:
        mil += 1
    if c == 1 or preço < prodB:
        prodB = preço
        prodBC = produto
    while cont not in 'SN':
        cont = str(input('Valor invalido, quer continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break
print('\nFIM DA LISTA\n')
print(f'O total da compra foi {total}.')
print(f'Temos {mil} produtos custando mais de R$: 1000.00.')
print(f'O produto mais barato foi {prodBC} que custa {prodB}.')