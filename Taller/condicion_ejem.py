# Crea una condición que te permita verificar si un valor es mayor o menor a 20
numero = int(input("Ingresa un número: "))

if numero > 20:
    print(f"El número {numero} es mayor que 20.")
elif numero < 20:
    print(f"El número {numero} es menor que 20.")
else:
    print(f"El número {numero} es igual a 20.")