#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTRIMETROS

valor = float(input('Digite um valor em metros que queria que seja convertido: '))

centimetros = valor / 100
milimetros = valor / 1000

print('O valor que você digitou é {}m, em centrímetros é {}cm e em milímetros ele é {}ml.'.format(valor, centimetros, milimetros))