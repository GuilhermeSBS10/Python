"""
Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km foram rodados no carro? '))

alugado = 60 * d
rodados = 0.15 * km

total = alugado + rodados

print('O valor total a pagar é de R${}'.format(total))

