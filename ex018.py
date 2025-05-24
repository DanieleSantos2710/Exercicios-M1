import math
a = float(input('Digite um angulo: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print("O seno do seu angulo é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}".format(s, c ,t))
