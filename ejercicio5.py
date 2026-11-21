horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
seg = int(input("Ingrese los segundos: "))

total_segundos = (horas * 3600) + (minutos * 60) + seg
print(f"El total expresado en segundos es: {total_segundos}")