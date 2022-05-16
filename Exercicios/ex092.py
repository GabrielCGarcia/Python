from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['Tem carteira de trabalho:'] = str(input('Tem CTPS: S/N ')).upper()
if dados['Tem carteira de trabalho:'] == 'S':
    dados['Ano de contratação'] = int(input('Qual o ano de Contratação: '))
    dados['Se aposentar com'] = str(dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)) + str(' anos.')
for k, v in dados.items():
    print(f'{k}: {v}')