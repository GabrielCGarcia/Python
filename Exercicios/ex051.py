termo = int(input('Diga o primeiro termo: '))
razão = int(input('Diga a razão: '))
for c in range(termo, termo + (10 * razão), razão):
    print(c)
print('Fim!')