'''
MANIPULAÇÃO DE TEXTO
'''

frase = 'guilherme santos'
print(frase[0])
print(frase[1])
print(frase[2])
print(frase[3])
print(frase[4])
print(frase[5])
print(frase[6])
print(frase[7])
print(frase[8])

print(frase[0:8])
print(frase[:8])
print(frase[8:])
print(frase[0:8:2])
print(frase[5::3])

len(frase)
frase.count('s')
frase.count(' ') # conta os espaços
frase.count('s',0,13)
frase.find('lh')
frase.find('apple')
'gui' in frase
frase.replace('guilherme', 'apple')
frase.upper() # TUDO MAIUSCULO
frase.lower() # tudo minusculo
frase.capitalize() # tudo minusculo e a primeira letra em MAIUSCULO
frase.title() # todo inicio de palavra com a letra Maiuscula
frase.strip() # remove os espaços no inícil e no fim da frases pois são inúteis
frase.rstrip() # remove os espaços da direita frases pois são inúteis
frase.lstrip() # remove os espaços da esquerda frases pois são inúteis
frase.split() # divide cada elementento pelos espaços e da um incie e se eu quiser chamar a str eu chamo pelo indice
'-'.join(frase)
