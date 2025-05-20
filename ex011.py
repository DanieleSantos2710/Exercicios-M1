altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

t = 2

r = area / t

print(' area da parede é {}, e você vai precisar de {} litros de tinta para pintar ela.'.format(area, r))
