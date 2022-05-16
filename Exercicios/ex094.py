listafinal = []
idademedia = []
mulheres = []
while True:
    lista = {'nome': str(input('Nome: ')),
            'sexo': str(input('Sexo M/F: '))}
    while lista['sexo'] not in "MmFf":
        lista['sexo'] = str(input('Erro! Por favor, digite apenas M ou F. ')).upper
    if lista['sexo'] in 'Ff':
        mulheres.append(lista['nome'])
    lista['idade'] = int(input('Idade: '))
    idademedia.append(lista['idade'])
    listafinal.append(lista)
    cont = str(input('Quer continuar S/N: '))
    while cont not in 'SsNn':
        cont = str(input('Erro! Por favor, digite apenas S ou N. ')).upper
    if cont in "Nn":
        break
pessoas = len(listafinal)
media = (sum(idademedia)) / (len(idademedia))
print(f'A) Ao todo temos {pessoas} cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print('D) Lista de pessoas que estão acima da média: ')
for lista in listafinal:
    if lista['idade'] >= media:
        for k, v in lista.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<<<ENCERRADO>>>>')