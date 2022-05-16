from tkinter import N


lista = [[], []]
for c in range(1,8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os valores par são: {sorted(lista[0])}')
print(f'Os valores ímpar são: {sorted(lista[1])}')