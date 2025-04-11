#CRIE UM ALGORÍTIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

n = float(input('Digite um numero: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('Visto o número que digitou, o dobro dele é {}, o triplo dele é {} e a raiz quadrada dele é {}'.format(dobro, triplo, raiz))