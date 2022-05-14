n = []
while True:
    num = int(input('Digite um valor: '))
    if num not in n:
        n.append(num)
        print('Valor adicionado.')
    else:
        print('Valor duplicado, portanto não foi adicionado.')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = (str(input('Valor invalido, quer continuar? [S/N] '))).strip().upper()
    if cont == 'N':
        break 
n.sort()
print(f'Os valores adicionados foram {n}')