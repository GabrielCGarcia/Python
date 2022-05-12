n = c = s = m = maior = menor = 0
ct = ''
while ct != 'N':
    n = int(input('Digite um número: '))
    ct = str(input('Quer continuar? [S/N] ')).strip().upper()
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
m = s / c
print('Você digitou {} números e a média foi {}\nO maior valor foi {} e o menor foi {}.'.format(c, m, maior, menor))
