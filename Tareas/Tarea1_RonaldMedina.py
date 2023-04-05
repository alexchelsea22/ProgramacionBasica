# Tarea # 1: Programacion Basica
# Proposito / Enunciado: Crear un diccionario con la informacion de un grupo de n estudiantes que contenga:
# Cedula, Sexo, y las notas obtenidas en varias asignaturas, donde, la cantidad de materias se generan aleatoriamente
# y las notas de las materias tambien, se solicita que se determine e imprima por consola:
# Promedio de notas por estudiante, Porcentaje de notas aprobadas por estudiante, y el estudiante con el mayor promedio
# Autor: Ronald Medina 
# Fecha de elaboracion: 11 / 02 / 2023

# Se importa random para poder generar los numeros aleatorios requeridos
import random

# Inicializacion de variables
alumnos = {}
promedios_alumnos = {}

# Datos de entrada
try:
    nro_alumnos = int(input("Ingrese cantidad de alumnos a registrar: "))
except:
    print("Valor no valido")
    quit()

# Proceso
for alumno in range(nro_alumnos):
    print("Registro del alumno nro:", (alumno + 1))
    cedula = input("Ingrese numero de cedula: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    sexo = input("Ingrese sexo: Masculino (M) - Femenino: (F): ")
    nro_asignaturas = random.randint(1,7)
    #print("Nro de asignaturas a registrar:", nro_asignaturas) #Mensaje que indica el nro de materias que tendra cada alumnos
    notas = []
    for asginatura in range(nro_asignaturas):
        notas.append(random.randint(0, 20))
        promedio = round(sum(notas) / nro_asignaturas, 2)
        aprobadas = 0
        for j in notas:
            if j >= 10:
                aprobadas += 1
        alumnos[cedula] = nombre, apellido, sexo, nro_asignaturas, notas, promedio, round(((aprobadas / nro_asignaturas)*100), 2) #Se agregan los datos de cada alumno
#print(alumnos)

print("Resultado del regsitro de alumnos: ")

# Datos de salida parte 1
for alumno in alumnos:
    print("Cedula:", alumno,"- Nombre:", alumnos[alumno][0],"- Apellido:", alumnos[alumno][1],"- Promedio:", alumnos[alumno][5], 
    "-% Asignaturas Aprobadas:", alumnos[alumno][6], "%") # Se imprimen los datos solicitados por cada estudainte
    # Se aprovecha el recorido del diccionario "alumnos", para generar un diccionario auxiliar con Cedula : Promedio
    promedios_alumnos[alumno] = alumnos[alumno][5] 

#print(promedios_alumnos)

# Datos de salida parte 2
max_promedio = max(promedios_alumnos.values()) # Se determina el valor del promedio maximo
alumno_max_promedio = max(promedios_alumnos, key = promedios_alumnos.get) # Se determina el alumno que tiene el promedio mas alto
print(f'El alumno con mayor promedio tiene cedula: {alumno_max_promedio} y tiene promedio de: {max_promedio}') # Variable de salida, calculo solicitado