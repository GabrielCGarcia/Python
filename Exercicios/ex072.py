num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont not in 'SN':
            cont = str(input(('Valor digitado incorreto, tente novamente: [S/N] '))).strip().upper()
        elif cont == 'S':
            continue
        else:
            print('Programa finalizado, obrigado!')
            break
    else:
        print('Tente novamente. ', end='')