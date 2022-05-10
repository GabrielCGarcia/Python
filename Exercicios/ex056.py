cidade = 0
csexo = 0
maior = 0
for c in range(1,5):
    print('---- {}° PESSOA ----'.format(c))
    nome = str.title(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str.upper(input('Sexo [M/F]: ')).strip()
    if sexo == 'M' and idade > maior:
        maior = idade
        cnome = nome
    cidade += idade
    if sexo == 'F' and idade <= 20:
        csexo += 1
print('A média de idade do grupo é de {:.1f} anos!'.format(cidade / c))
if maior > 0:
    print('O homem mais velho tem {} anos e se chama {}!'.format(maior, cnome))
if csexo == 1:
    print('Ao todo temos 1 mulher com 20 anos ou menos!')
else:
    print('Ao todo temos {} mulheres com 20 anos ou menos!'.format(csexo))