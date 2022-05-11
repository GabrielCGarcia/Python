S = str.upper(input('Informe seu sexo: [M/F] ')).strip()[0]
while S != 'M' and S != 'F':
    S = str.upper(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()[0]
print('Sexo {} registrado com sucesso.'.format(S))