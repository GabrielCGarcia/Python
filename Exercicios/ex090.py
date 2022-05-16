aluno = {}
escola = []
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
escola.append(aluno.copy())
for k, v in aluno.items():
    print(f'- {k} é {v}.')
if aluno['media'] < 7.0:
    print('Aluno reprovado!')
elif 5.0 > aluno['media'] < 7.0:
    print('Aluno em recuperação!')
else:
    print('Aluno aprovado!')