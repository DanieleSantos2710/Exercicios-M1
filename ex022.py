name = str(input('Digite seu nome completo: '))

maiusculo = name.upper()
minusculo = name.lower()

letras = name.split()[0]
conta = len(letras)

sem = name.replace(" ", "")
sem2 = len(sem)

print('Maiusculo {}'.format(maiusculo))
print('Minusculo {}'.format(minusculo))
print('Letras no primeiro nome {}'.format(conta))
print('Numero de letras ao todo {}'.format(sem2))
