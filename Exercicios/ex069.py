print('\nCADASTRE UMA PESSOA!\n')
maiorI = Mmenor = homens = 0
cont = ''
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF':
        print('Valor inserido invalido, tente novamente. [M/F] ')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade > 17:
        maiorI += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        Mmenor += 1
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        print('Valor inserido invalido, tente novamente. [S/N] ')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {maiorI}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {Mmenor} mulheres com menos de 20 anos cadastradas.')