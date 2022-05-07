num = int(input('Digite um número e irei adivinhar se é par ou impar: '))
resto = num % 2
if resto == 0:
    print('Seu número é par!')
else: 
    print('Seu número é impar!')