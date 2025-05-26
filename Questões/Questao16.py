"""
Crie um programa que leia dois números sendo um o cateto oposto e o outro o
cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da
hipotenusa.
"""

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)

print('O valor do CO e do CA são respectivamente {},{} e o valor da hipotenusa é {}'.format(co, ca, h))

