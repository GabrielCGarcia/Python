preço = float(input('Qual o preço atual do produto? R$: '))
porcentagem = int(input('Qual a quantidade de desconto que vai ser usado? '))
desc = preço * (porcentagem / 100)
print('O valor do item era R$:{:.2f}, o desconto escolhido foi {:.2f} e o valor final ficou R$:{:.2f}!'.format(preço,porcentagem,desc))