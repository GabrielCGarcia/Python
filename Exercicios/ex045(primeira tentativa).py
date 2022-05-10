from random import choice
from time import sleep

print('Vamos jogar Pedra, Papel, Tesoura!')
player = str(input('Suas opções:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nQual é a sua jogada? '))

print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PO!')

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(jogadas)

if player == '1' and pc == 'TESOURA':
    print('Você escolheu PEDRA.')
    sleep(0.5)
    print('O PC escolheu TESOURA.')
    sleep(0.5)
    print('Você ganhou!')
elif player == '1' and pc == 'PAPEL':
    print('Você escolheu PEDRA.')
    sleep(0.5)
    print('O PC escolheu PAPEL.')
    sleep(0.5)
    print('Você perdeu!')
elif player == '1' and pc == 'PEDRA':
    print('Você escolheu PEDRA.')
    sleep(0.5)
    print('O PC também escolheu PEDRA.')
    sleep(0.5)
    print('Deu empate!')