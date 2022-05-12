from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
op = 0
while op != 5:
    print('=-='*10)
    print('''   ---[MENU]---
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Qual a sua opção? '))
    print('=-='*10)
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif op == 3:
        if n1 < n2:
            print('O maior número é o {}.'.format(n2))
        elif n1 == n2:
            print('Os dois números são iguais.')
        elif n1 > n2:
            print('O maior número é o {}.'.format(n1))
    elif op == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção invalida!')
print('>>Programa finalizado, obrigado!\n')