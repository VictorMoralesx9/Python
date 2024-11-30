# Crea un ciclo que me muestre los números pares desde 0 hasta un valor que se ingrese por teclado.
valor = int(input("Ingresa un número: "))
for i in range(0, valor + 1, 2):  # El 2 es el paso para ir solo en pares
    print(i)
    