from random import randint
print('VAMO JOGAR PAR OU ÍMPAR?')
print('')
cD = 0
cV = 0
while True:
    jogador = int(input('Diga um valor: '))
    jogador2 = str(input('Diga se é par ou ímpar: [P/I] ')).strip().upper()
    computador = randint(0,10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    parimpar = total % 2
    if parimpar == 0:
        if jogador2 == 'P':
            print('Parabéns, você acertou, a soma deu Par!')
            cV += 1
        elif jogador2 == 'I':
            print('Errou, a soma deu Par')
            cD += 1
    if cD == 1:
        break
    elif parimpar == 1:
        if jogador2 == 'I':
            print('Parabéns, você acertou, a soma deu Ímpar!')
            cV += 1
        elif jogador2 == 'P':
            print('Errou, a soma deu Ímpar')
            cD += 1
    if cD == 1:
        break
print(f'Fim de jogo, você acertou {cV} rodadas consecutivas!')