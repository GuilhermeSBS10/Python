
l1 = float(input("digite o primeiro lado: "))
l2 = float(input("digite o segundo lado: "))
l3 = float(input("digite o terceiro lado: "))

if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print("O trinângulo é inválido: ")

if l1 == l2 == l3:
    print("O triangulo é válido e equilátero.")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("O triangulo é isóceles.")
else: 
    print("O triângulo é escaleno: ")
    


