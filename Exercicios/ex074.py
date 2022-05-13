print('Modo de fazer 1.')
from random import choice
n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
c = maior = menor = cont =0
print('Os valores sorteados foram: ' ,end='')
while True:
    nr = choice(n)
    print(f'{nr}, ', end='')
    cont += 1
    c += 1
    if cont == 1 or nr > maior:
        maior = nr
    if cont == 1 or nr < menor:
        menor = nr
    if c == 5:
        break
print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')

# ou podemos fazer assim: 
print('\nModo de fazer 2.')

from random import sample
numeros = tuple((sample(range(0, 11), 5)))
print(f'Os valores sorteados foram: {numeros}.')
print(f'O maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')