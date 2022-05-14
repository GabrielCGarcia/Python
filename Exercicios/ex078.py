#Modo 1 de fazer utilizando Numpy e Array
import numpy as np
n = [int(input('Digite um valor para a posição 0: ')),
     int(input('Digite um valor para a posição 1: ')),
     int(input('Digite um valor para a posição 2: ')),
     int(input('Digite um valor para a posição 3: ')),
     int(input('Digite um valor para a posição 4: '))]
n = np.array(n)
print(f'Você digitou os valores: {n}, ')
max = max(n)
min = min(n)
resultmax = np.where(n == max)
resultmin = np.where(n == min) 
print(f'O maior valor digitado foi {max} nas posições: {resultmax[0]}.')
print(f'O menor valor digitado foi {min} nas posições: {resultmin[0]}.')

print('\n\n')

#Modo 2 de fazer utilizando apenas lista
listanum = []
mai = men = 0
for c in range(0, 5):
     listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
     if c == 0:
          mai = men = listanum[c]
     else:
          if listanum[c] > mai:
               mai = listanum[c]
          if listanum[c] < men:
               men = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições: ', end='')
for i, v in enumerate(listanum):
     if v == mai:
          print(f'{i}, ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
     if v == men:
          print(f'{i}, ', end='')
print()