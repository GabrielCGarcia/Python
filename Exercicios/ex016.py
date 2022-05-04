import math
#Modo 1 de fazer a quebra do número
num1 = float(input('Digite um numero1 e mostrarei a porção inteira: '))
print('Seu número é o {} e a sua porção inteira é {:.0f}'.format(num1, num1)) 

#Modo 2 de fazer a quebra do número
num2 = float(input('Digite um numero2 e mostrarei a porção inteira: '))
print('Seu número é o {} e a sua porção inteira é {}'.format(num2, math.trunc(num2)))

#Modo 3 de fazer a quebra do número
num3 = float(input('Digite um numero3 e mostrarei a porção inteira: '))
print('Seu número é o {} e a sua porção inteira é {}'.format(num3, int(num3)))