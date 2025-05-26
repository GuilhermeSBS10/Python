"""
Faça um programa que leia varios nomes e sortei uma sequência da lista de nomes que colocou
"""

import random

lista = []
contador = 0
numero = int(input('Digite quantos nomes você quer digitar na lista: '))

while contador < numero:

  N = input('Digite um nome: ')
  lista.append(N)
  contador = contador + 1

print('Essa foi a lista que vc digitou: ', lista)

random.shuffle(lista)

print('A lista embaralhada ficou: {}'.format(lista))


