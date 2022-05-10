from random import choice
from time import sleep

escolha = str(input('''Suas opções:
 [1] PEDRA
 [2] PAPEL
 [3] TESOURA
  Qual é a sua jogada? '''))

if escolha == '1':
    escolha = 'PEDRA'
elif escolha == '2':
    escolha = 'PAPEL'
elif escolha == '3':
    escolha = 'TESOURA'
else:
    print('Valor informado incorreto, tente novamente!')

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(jogadas)

if (escolha == 'PEDRA' and jogadas == 'PEDRA') or (escolha == 'PAPEL' and jogadas == 'PAPEL') or (escolha == 'TESOURA' and jogadas == 'TESOURA'):
    print('Você encolheu {} e o PC escolheu {}!'.format(escolha, pc))
    print('Deu empate!')

elif (escolha == 'PAPEL' and jogadas == 'PEDRA') or (escolha == 'TESOURA' and jogadas == 'PAPEL') or (escolha == 'PEDRA' and jogadas == 'TESOURA'):
    print('Você encolheu {} e o PC escolheu {}!'.format(escolha, pc))
    print('Você ganhou!')

elif (escolha == 'TESOURA' and jogadas == 'PEDRA') or (escolha == 'PEDRA' and jogadas == 'PAPEL') or (escolha == 'PAPEL' and jogadas == 'TESOURA'):
    print('Você encolheu {} e o PC escolheu {}!'.format(escolha, pc))
    print('Você perdeu!')