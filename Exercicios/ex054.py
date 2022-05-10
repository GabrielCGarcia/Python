from datetime import date
ano = date.today().year
maior = 0
menor = 0
error = 0
for c in range (1,8):
    p = int(input('Em que ano a {}° pessoas nasceu? '.format(c)))
    if p > ano or p < 1900:
        error += 1
    elif ano - p < 18:
        menor += 1
    else:
        maior += 1
if menor == 0:
    print('Todos os {} valores informados são maiores de idade!'.format(maior))
elif maior == 0:
    print('Todos os {} valores informados são menores de idade!'.format(menor))
else:
    print('Ao todo tivemos {} pessoas maiores de idade!'.format(maior))
    print('Ao todo tivemos {} pessoas menores de idade!'.format(menor))
if error > 0:
    print('Foi inserido valores menores que 1900 ou maiores que {} um total de {} vezes, esses foram desconsiderados!'.format(ano, error))