import random

a1 = str(input('Diga o nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))

lista = [a1, a2, a3, a4]

r = random.choice(lista)

print('O aluno escolhido foi {}'.format(r))
