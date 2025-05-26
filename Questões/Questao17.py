"""
Faça um programa que leia varios nomes e sortei um deles para ser o escolhido.
"""
import random
import math

lista_nomes = []

n = int(input('Digite quantos nomes você quer sortear: '))
c = 0


while c < n :
  i = str(input('Digite um nome por vez: '))
  lista_nomes.append(i)
  c = c + 1



print(lista_nomes)
sorteio = random.choice(lista_nomes)

print('O nome escolhido foi {}'.format(sorteio))

