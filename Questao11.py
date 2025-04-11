"""
Faça um programa que calcule o aumento ou o decrécimo de um salário
"""

almento_ou_decremento = str(input('Digite (a) para aumento ou (d) para decremento: '))

if almento_ou_decremento == 'a':
  salario = float(input('Digite o valor do salário: R$'))
  aumento = float(input('Digite o valor do aumento em %: '))
  mais = salario + (salario * (aumento/100))
  print('O valor do salário era {} mas com o aumento de {}% fica um valor final de: {}'.format(salario, aumento, mais))
elif almento_ou_decremento == 'd':
  salario = float(input('Digite o valor do salário: R$'))
  decremento = float(input('Digite o valor do decremento em %: '))
  menos = salario - (salario * (decremento/100))
  print('O valor do salário era {} mas com o decremento de {}% fica um valor final de: {}'.format(salario, decremento, menos))
else:
  print('Opção inválida')
