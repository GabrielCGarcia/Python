nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
nomeM = nome.upper()
print('Seu nome em maiúsculas é {}'.format(nomeM))
nomem = nome.lower()
print('Seu nome em minúsculas é {}'.format(nomem))
nomecount = (len(nome) - nome.count(' '))
print('Seu nome tem ao todo {} letras'.format(nomecount))
nomesep = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomesep[0], len(nomesep[0])))