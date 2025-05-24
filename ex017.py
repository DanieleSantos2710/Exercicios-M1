import math

c1 = float(input('Digite o comprimento do primeiro cateto: '))
c2 = float(input('Digite o segundo comprimento: '))

''' h = (c1 ** 2 + c2 ** 2) ** (1/2)'''

h = math.hypot(c1, c2)

print('A soma dos catos é {:.2f}'.format(h))
