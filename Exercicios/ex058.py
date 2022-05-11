import random

print('Estou pensando em um número entre 1 e 10, tente adivinhar qual é...')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #N de número
r = int(input('Digite o número: ')) #R de resposta
s = random.choice(n) #S de sorteio
c = 0 #C de contador
while r != s:
    if r < s:
        r = int(input('Errou, é um número maior, tente novamente: '))
        c += 1
    if r > s:
        r = int(input('Errou, é um número menor, tente novamente: '))
        c += 1
if c == 1:
    print('Parabéns, você acertou após 1 tentativa, foi excelente!')
elif c > 1 and c < 3:
    print('Parabéns, você acertou após {} tentativas, mas podia ter sido melhor em!'.format(c))
elif c > 3:
    print('Eita, você precisou de {} tentativas, mandou mal em haha! Boa sorte na proxima!'.format(c))