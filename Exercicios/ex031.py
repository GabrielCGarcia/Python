vel = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma de {}Km/h'.format(vel))
if vel > 200:
    print('E o preço da sua passagem será de R$: {:.2f}!'.format(vel * 0.45))
else:
    print('E o preço da sua passagem será de R$: {:.2f}!'.format(vel * 0.5))