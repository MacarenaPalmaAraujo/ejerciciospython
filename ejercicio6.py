DIVISOR = 2  # Constante por convención

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

superficie = (base * altura) / DIVISOR
print(f"La superficie del triángulo es: {superficie}")