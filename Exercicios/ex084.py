lista = []
dados = []
pessoas = 0
mais = menos = 0
big = []
small = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if pessoas == 0:
          mais = menos = peso
    else:
        if peso > mais:
               mais = peso
               big.append(nome)
        if peso < menos:
               menos = peso
               small.append(nome)
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    pessoas += 1
    cont = str(input('Quer continuar? S/N ')).strip().upper()
    while cont not in "SN":
            cont = str(input('Comando invalido, quer continuar? S/N ')).strip().upper()
    if cont == 'N':
        break
print(f'Foram cadatradas {pessoas} pessoas!')
print(f'O maior peso foi {mais}, sendo {big}')
print(f'O menos peso foi {menos}, sendo {small}')