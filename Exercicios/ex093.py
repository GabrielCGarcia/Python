jogador = {}
partidas = []
jogador['Nome'] = str(input('Qual o nome do jogador? '))
tot = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for c in range(1, tot+1):
    partidas.append(int(input(f'Quantas gols na {c}° partida? ')))
jogador['Gols'] = partidas[:]
jogador['Total de gols'] = sum(partidas)
print('=-='*15)
print(jogador) 
print('=-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.') 
print('=-='*15)
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas!')
for c in range(0, tot):
    print(f'Na {c+1}° partida fez {partidas[c]} gols.')
print(f'Foi um total de {sum(partidas)} gols.')