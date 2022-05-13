n = (int(input('Digite um número:')),
     int(input('Digite um número:')),
     int(input('Digite um número:')),
     int(input('Digite um número:')))
print(f'Você digitou os valores {n}.')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O 1° valor 3 apareceu na posição {n.index(3)+1} ')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(f'{num}, ', end='')