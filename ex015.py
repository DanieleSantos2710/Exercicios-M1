d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
p = (d * 60) + (km * 0.15)
print('O total para pagar R${:.2f}'.format(p))
