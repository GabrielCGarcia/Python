print('Para calcular seu IMC (kg/m²) preenche os campos abaixo:')
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura: (m e cm) '))
IMC = peso / (altura * altura)
print('O seu IMC é {:.1f}!'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso!')
elif IMC <= 25:
    print('Você está no seu peso ideal, parabéns!')
elif IMC <= 30:
    print('Você está com sobrepeso!')
elif IMC <= 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')