idade = int(input("Digite sua idade por favor: "))

if idade < 3 and idade > 0:
    print("------------------------------")
    print ("ENTRADA GRÁTIS, DIVIRTA-SE")
    print("------------------------------")
elif idade > 3 and idade <= 12:
    print("------------------------------")
    print("ENTRADA DE CRIANÇA")
    print("------------------------------")
elif idade > 12 and idade <= 17:
    print("------------------------------")
    print("INGRESSO DE ADOLESCENTE")
    print("------------------------------")
elif idade > 17 and idade <= 59:
    print("------------------------------")
    print("INGRESSO ADULTO")
    print("------------------------------")
elif idade > 59:
    print("------------------------------")
    print("INGRESSO IDOSO")
    print("------------------------------")
else:
    print("------------------------------")
    print("INGRESSO INVÁLIDO")
    print("------------------------------")