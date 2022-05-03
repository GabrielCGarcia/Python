largurap = float(input('Largura da parede em metros: '))
alturap = float(input('Altura da parede metros: '))
area = alturap * largurap
ltinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largurap,alturap,area))
print('Para pintar sua parede será necessario {:.2f} litros de tinta.'.format(ltinta))