"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela quantas unidades, dezenas, centenas e milhares.
"""

num  = int(input('Digite um número de 0 a 9999: '))

unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))