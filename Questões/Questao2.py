#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.

n = int(input('Digite um número: '))

n1 = n - 1
n2 = n + 1

print('Você digitou o numero {} e o número antes dele é o {} e o número depois dele é o {}'.format(n, n1, n2))