vel = int(input('Qual a velocidade atual do carro? '))
if vel <= 80:
    print('Você está dentro da velocidade, tenha um bom dia!')
else:
    multa = (vel - 80) * 7
    print('Você excedeu o limite determinado que é de 80Km/h.\n Você deve pagar a multa de R$: {}!'.format(multa))