"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a
sua porção inteira (TRUNC)
"""
import math
num = float(input('Digite um número real qualquer (tem que ser um número Real e escrito com o ponto e n com virgula ok?): '))
numinteiro = math.trunc(num)
print('O numero digitado foi {} e a parte inteira dele é {}'.format(num, numinteiro))