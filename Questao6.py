#FAÇA UM PROGRAMA QUE CONVERTA DE METROS PARA TODAS AS OUTRAS MEDIDAS

m = float(input('Digite um valor em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('-----------------------------------------------------------------')
print('O valor {}m convertido em outras medidas de comprimentos fica: '.format(m))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
print('-----------------------------------------------------------------')