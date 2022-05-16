from random import randint
jogos = int(input('Quantos jogos você quer que eu sorteie: '))
result = []
for v in range(jogos):
    while len(result) != 6:
        r = randint(1, 60)
        if r not in result:
            result.append(r)
    print(f'Jogo {v+1}: {sorted(result)}')
    result.clear()