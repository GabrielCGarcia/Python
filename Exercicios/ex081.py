lista = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    cont = str(input('Quer continuar? S/N ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Resposta invalida, quer continuar? S/N ')).strip().upper()
    if cont == 'N':
        break
print(f'Você digitou {c} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')