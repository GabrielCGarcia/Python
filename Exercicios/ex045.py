from random import choice
from time import sleep

print('Vamos jogar Pedra, Papel, Tesoura!')
print('Suas opções:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')

player = int(input('Qual é a sua jogada? '))

if player == 1:
    print('Você escolheu PEDRA')
elif player == 2:
    print('Você escolheu PAPEL')
elif player == 3:
    print('Você escolheu TESOURA')
else:
    print('Valor informado incorreto, tente novamente!')
sleep(0.5)

print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PO!')

pc0 = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(pc0)
sleep(0.5)
print('O PC escolheu {}!'.format(pc))
sleep(0.5)

if (player == 1 and pc == 'PEDRA') or (player == 2 and pc == 'PAPEL') or player == 3 and pc == 'TESOURA':
    print('Deu empate!')
elif (player == 2 and pc == 'PEDRA') or (player == 3 and pc == 'PAPEL') or player == 1 and pc == 'TESOURA':
    print('Você ganhou!')
elif (player == 3 and pc == 'PEDRA') or (player == 1 and pc == 'PAPEL') or player == 2 and pc == 'TESOURA':
    print('Você perdeu!')