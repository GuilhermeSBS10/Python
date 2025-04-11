"""
Faça um programa que converta uma temperatura digitada em °C e converta para °F e K
"""

c = float(input('Digite a temperatura em °C: '))

f = (c * 1.8) + 32
k = c + 273

print('A temperatura em °F é {} e em K é {}'.format(f, k))
