from datetime import datetime

def calcular_edad(fecha_nacimiento):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Restar el año de nacimiento al año actual
    edad = fecha_actual.year - fecha_nacimiento.year
    # Verificar si ya pasó el cumpleaños este año
    if fecha_actual.month<fecha_nacimiento.month & fecha_actual.day < fecha_nacimiento.day:
        edad -= 1
    return edad

# Solicitar al usuario la fecha de nacimiento en formato (dd-mm-yyyy)
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (dd-mm-yyyy): ")
# Convertir el string ingresado a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d-%m-%Y")

# Calcular la edad y mostrar el resultado
edad = calcular_edad(fecha_nacimiento)
print(f"Tienes {edad} años.")
