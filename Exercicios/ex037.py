n = int(input('Escreva um número inteiro qualquer: '))
print('Escolha a conversão abaixo:\n[1] para binário\n[2] para octal\n[3] hexadecimal:')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('Seu número em binario é: {}'.format(bin(n) [2:]))
elif escolha == 2:
    print('Seu número em octal é: {}'.format(oct(n) [2:]))
elif escolha == 3:
    print('Seu número em hexadecimal é: {}'.format(hex(n) [2:]))
else:
    print('Opção invalida!')