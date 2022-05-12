termo = int(input('Diga o primeiro termo: '))
razão = int(input('Diga a razão: '))
c = 0
print('O termo escolhido foi {} e a razão {}.'.format(termo,razão))
while c < 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    c += 1
print('Fim!')