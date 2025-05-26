"""
Faça um programa que fale o preço de um produto antes e depois da promoção
"""
print('..................................................................................')
p = float(input('Qual o preo do produto? R$'))
d = float(input('Qual o valor do desconto em %?'))

pd = p - (p * (d/100))

print('O valor do produto era {} mas com o desconto de {}% fica um valor final de: {}'.format(p, d, pd))
print('..................................................................................')