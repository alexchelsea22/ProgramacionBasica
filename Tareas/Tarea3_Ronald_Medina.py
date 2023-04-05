# Tarea # 3 #: Programacion Basica
# Proposito / Enunciado: Crear un archivo con la informacion de un grupo de n estudiantes que contenga:
# Cedula, Sexo, y las notas obtenidas en varias asignaturas, donde, la cantidad de materias se generan aleatoriamente
# y las notas de las materias tambien, se solicita que se determine e imprima por consola:
# Promedio de notas por estudiante, Porcentaje de notas aprobadas por estudiante, y el estudiante con el mayor promedio
# Autor: Ronald Medina 
# Fecha de elaboracion: 17 / 02 / 2023


def imprimir(archivo, cedula, nombre, apellido, sexo, nro_asignaturas, notas, promedio, por_aprobadas):
    #Funcion que imprimi una linea en el archivo con todos los datos de un alumno
    archivo.write(f'{cedula}, {nombre}, {apellido}, {sexo}, {nro_asignaturas}, {notas}, {promedio}, {por_aprobadas} \n')


def main():
    import random # Se importa random para poder generar los numeros aleatorios requeridos

    # Inicializacion de variables
    alumnos = {}
    bandera = 0
    promedio_mayor = 0
    alumno_promedio_mayor = ""
    resultados = open("alumnos.txt", "w") #Apertura del archivo
   
    # Datos de entrada
    try:
        nro_alumnos = int(input("Ingrese cantidad de alumnos a registrar: ")) #Se registra el numero de alumnos a registrar
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
        notas = []
        for _ in range(nro_asignaturas):
            notas.append(random.randint(0, 20))
            promedio = round(sum(notas) / nro_asignaturas, 2)
            aprobadas = 0
            for j in notas:
                if j >= 10:
                    aprobadas += 1
            alumnos[cedula] = nombre, apellido, sexo, nro_asignaturas, notas, promedio, round(((aprobadas / nro_asignaturas)*100), 2) #Se agregan los datos de cada alumno
    
    #Datos de salida registro en el archivo del datos de los alumnos
    for alumno in alumnos: #ciclo para imprimir en el archivo
        imprimir(resultados, alumno, alumnos[alumno][0], alumnos[alumno][1], alumnos[alumno][2], alumnos[alumno][3], alumnos[alumno][5], alumnos[alumno][6], alumnos[alumno][4])
        if bandera == 0: #se usa la bandera para determinar el alumno con mayor promedio
            bandera = 1
            alumno_promedio_mayor = alumno
            promedio_mayor = alumnos[alumno][5]
        elif alumnos[alumno][5] > promedio_mayor:
            alumno_promedio_mayor = alumno
            promedio_mayor = alumnos[alumno][5]
    print("El alumno con mejor promedio es", alumno_promedio_mayor, "con promedio de", promedio_mayor)  
    
    resultados.close() #Cierre del archivo

if __name__ == "__main__": #Llamado a programa subprograma principal
    main()