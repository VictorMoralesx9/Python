# Crea una condición que evalué 2 posibilidades
numero = int(input("Ingresa un número: "))

if numero % 2 == 0 and numero > 10:
    print(f"El número {numero} es par y mayor que 10.")
elif numero % 2 == 0:
    print(f"El número {numero} es par pero no es mayor que 10.")
else:
    print(f"El número {numero} no es par.")