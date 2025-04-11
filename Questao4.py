#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALINO, CALCULE E MOSTRE A SUA MÉDIA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A media entre as duas notas, sendo a primeira {} e a segunda {} é {}'.format(n1, n2, media))