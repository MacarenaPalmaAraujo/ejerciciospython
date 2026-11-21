fecha = int(input("Ingrese la fecha en formato DDMMAAAA: "))

anio = fecha % 10000
aux = fecha // 10000
mes = aux % 100
dia = aux // 100

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")