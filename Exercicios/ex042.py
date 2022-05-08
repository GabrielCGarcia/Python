from datetime import date
ano = date.today().year
bday = int(input('Veja em qual categoria você se enquadra abaixo\nDiga seu ano de nascimento: '))
idade = ano - bday
print('Se você nasceu no ano de {} você tem {} anos, sendo assim sua categoria é:'.format(bday, idade))

if idade <= 0 or idade >= 100:
    print('Valor invalido, digite novamente por favor.')
elif idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
        print('Categoria: SÊNIOR')
elif idade > 25:
        print('Categoria: MASTER')
if idade >= 1 and idade < 100:
    print('Obrigado por consultar a sua categoria :)')