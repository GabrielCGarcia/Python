import math
ang = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O Seno é {:.2f}\nO cosseno é {:.2f}\nA tangente {:.2f}'.format(seno,cosseno,tangente))