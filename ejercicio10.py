nota_parcial = float(input("Ingrese nota de exámenes parciales (0 a 10): "))
nota_tp = float(input("Ingrese nota de trabajos prácticos (0 a 10): "))
nota_integrador = float(input("Ingrese nota de examen integrador (0 a 10): "))

nota_final = (nota_parcial * 0.30) + (nota_tp * 0.20) + (nota_integrador * 0.50)
print(f"La calificación final es: {nota_final}")