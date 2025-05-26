#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.

n = int(input('Digite um número para ver sua tabuada: '))

contador = 0

print('-----------')
while contador <= 10:
  print('{} x {} = {}'.format(n, contador, n * contador))
  contador += 1
print('-----------')
