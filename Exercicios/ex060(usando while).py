from math import factorial
n = int(input('Digite um número para cacular seu fatorial: '))
f = factorial(n)
c = n
print('O valor informado foi {}.'.format(n))
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}.'.format(f))