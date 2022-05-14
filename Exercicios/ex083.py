res = str(input('Digite a expressão: '))
a = 0
f = 0
for par in expr:
    if par == '(':
        a += 1
    elif par == ')':
        f += 1
if a - f == 0:
    print('A sua expressão está correta.')
else:
    print('A sua expressão está errado.')