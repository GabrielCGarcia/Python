print('Estou pensando em um número entre 1 e 5, tente adivinhar qual é...')
import random
from time import sleep
n = [1, 2, 3, 4, 5]
res = int(input('Digite o número: '))
sorteio = random.choice(n)
print('Pensando...')
sleep(3)
print('O número que eu escolhi foi {}'.format(sorteio))
if res == sorteio:
    print('Parabéns, você acertou!')
else: 
    print('Mandou mal, você errou!')