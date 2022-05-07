sal = float(input('Qual é o salario do funcionario: R$: '))
if sal < 1500:
    print('Quem ganhava R$: {:.2f} passa a ganhar R$: {:.2f}!'.format(sal, sal * 1.15))
else:
    print('Quem ganhava RS {:.2f} passa a ganhar R$: {:.2f}!'.format(sal, sal * 1.10))