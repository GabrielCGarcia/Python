r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))

if r1 == r2 == r3:
    print('Seu triangulo é Equilátero!')
elif r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('As retas informadas não podem fomar um triangulo!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Seu triangulo é Isósceles!')
else:
    print('Seu triangulo é Escaleno!')