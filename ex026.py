frase = str(input('Digite qualquer frase: ')).lower().strip()
conta = frase.count('a')
pri = frase.find('a')+1
ul = frase.rfind('a')+1

print ('A letra > a < aparece {} no texto. \nEla aparece na primeira vez na posição {} do texto \nEla aparece pela ultima vez na posição {}'.format(conta, pri, ul))