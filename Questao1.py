#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçções possíveis sobre ele

a = input('Digite qualquer coisa: ')

print ('O tipo da variável a é: ', type(a))
print ('Só tem espaços? ', a.isspace())
print ('É um número? ', a.isnumeric())
print ('É alfabético? ', a.isalpha())
print ('É alfanumérico? ', a.isalnum())