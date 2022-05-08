import datetime

ano = datetime.date.today().year
alistamento = str.lower(input('Você já alistou no exercito? '))

if alistamento == 'sim':
    print('Ok, obrigado por ajudar o país!')
elif alistamento == 'não' or 'nao':
    idade = int(input('Diga a sua idade: '))
    tempo = idade - 18
    print('Você nasceu em {}.'.format(ano - idade))
    if tempo >= 1:
        print('Já passou do tempo de você se alistar, você devia ter se alistado em {}.'.format(ano - tempo))
    elif tempo < 0:
        print('Você ainda não está na idade, você deve comparecer ao batalhão mais proximo no ano de {}.'.format(ano - idade + 18))
    else:
        print('Você está no ano de alistamento, vá ao batalhão mais proximo IMEADIATAMENTE!')
else:
    print('Resposta invalida.')
