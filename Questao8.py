#FAÇA UM CONVERSOR DE MOEDAS QUE IDENTIFIQUE A MOEDA E CONVERTA PARA REAL, DOLAR, EURO E PESOS ARGENTINOS
import sys

print('-------------------------------')
print('Digite (r) para real')
print('Digite (d) para dólar')
print('Digite (e) para euro')
print('Digite (a) para peso argentino')
print('Digite (s) para sair')
print('-------------------------------')

m = str(input('Digite qual moeda que deseja converter ou se quer sair do programa: '))

if m == 's':
  print('Saindo...')
  sys.exit()
q = float(input('Digite o valor que deseja converter: '))

if m == 'r':
  d = q / 6
  print('O valor de {} em dolar é: {}'.format(m, d))
  e = q / 7
  print('O valor de {} em euro é: {}'.format(m, e))
  a = q * 182
  print('O valor de {} em peso argentino é: {}'.format(m, a))
elif m == 'd':
  r = q * 6
  print('O valor de {} em real é: {}'.format(m, r))
  e = q / 0.95
  print('O valor de {} em euro é: {}'.format(m, e))
  a = q * 1060
  print('O valor de {} em peso argentino é: {}'.format(m, a))
elif m == 'e':
  r = q * 7
  print('O valor de {} em real é: {}'.format(m, r))
  d = q * 1.05
  print('O valor de {} em dólar é: {}'.format(m, d))
  a = q * 1115
  print('O valor de {} em peso argentino é: {}'.format(m, a))
elif m == 'a':
  r = q / 182
  print('O valor de {} em real é: {}'.format(m, r))
  d = q / 1060
  print('O valor de {} em dólar é: {}'.format(m, d))
  e = q / 1115
  print('O valor de {} em euro é: {}'.format(m, e))
else:
  print('Opção inválida')