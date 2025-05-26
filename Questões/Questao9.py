"""
Faça um programa que ajude pessoas a pintar uma parede, sabendo que 1m³ é
equivalente a 0,5L de tinta.
"""

print('Vamos calcular quantos litros de tinta vai ser usada na sua parede')

h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))

area = h * l
litros = area / 0.5

print('--------------------------------------------------------)')
print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(h, l, area))
print('Você vai precisar de {}L de tinta para pintar a parede'.format(litros))
print('--------------------------------------------------------)')