lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Comando invalido, quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')