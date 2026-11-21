cant_autos = int(input("Ingrese la cantidad de autos vendidos: "))
valor_auto = float(input("Ingrese el valor de venta de la unidad: "))

comision_fija = cant_autos * 200
comision_porcentaje = (cant_autos * valor_auto) * 0.05
salario_total = 5500 + comision_fija + comision_porcentaje

print(f"El salario total del vendedor es: ${salario_total}")