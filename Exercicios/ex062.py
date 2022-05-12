termo = int(input('Diga o primeiro termo: '))
razão = int(input('Diga a razão: '))
c = 1
print('O termo escolhido foi {} e a razão {}.'.format(termo,razão))
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        c += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('Foram mostrados {} progressões. Fim!'.format(c))