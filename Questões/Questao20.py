"""
Faça um programa que mostre diversas variedades sobre o nome de alguêm
"""

nome = str(input('Digite seu nome completo se quiser: '))

print('Seu nome com letras maiúsculas é: '+nome.upper())
print('Seu nome com letras minúsculas é: '+nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


