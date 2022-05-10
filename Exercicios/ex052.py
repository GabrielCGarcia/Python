n = int(input('Diga um número inteiro e direi se é número primo: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print('O número é PRIMO!')
else:
    print('O número NÂO É PRIMO!')