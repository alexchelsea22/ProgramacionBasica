# Tarea # 4 #: Programacion Basica
# Proposito / Enunciado: Crear un CRUD en sqlite3 utilizando como base los datos registrados de los estudiantes en la tarea N° 1
#Los campos que debe poseer cada estudiante son los siguientes:
#Cedula, Nombre, Apellido , Sexo, nro de asignaturas, promedio, % de materias aprobadas, y lista de notas
# Autor: Ronald Medina 
# Fecha de elaboracion: 28 / 02 / 2023

import sqlite3

#Funciones del CRUD
def agregar_alumno():
    #Agrega un alumno al sistema ingresando los datos manualmente
    try:
        conexion = sqlite3.connect("alumnos.sqlite") #"alumnos2.db
        cursor = conexion.cursor()
        while(True):
            print("Ingrese datos del nuevo registro: ")
            cedula = input("Ingrese cedula: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            sexo = input("Ingrese sexo: ")
            nro_asignaturas = input("Ingrese numero de asignaturas: ")
            promedio = input("Ingrese promedio: ")
            porc_aprobadas = input("Ingrese porcentaje de materias aprobadas: ")
            notas = input("Ingrese lista de notas: ")
            data = (cedula, nombre, apellido, sexo, nro_asignaturas, promedio, porc_aprobadas, notas,)
            query = "INSERT into Alumnos (cedula, nombre, apellido, sexo, nro_asignaturas, promedio, porc_aprobadas, notas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, data)
            conexion.commit()
            aux = input("Desea agregar otro registro? (S/N): ") 
            if aux == "N" or aux == "n":
                cursor.close()
                break
            else:
                pass
    except:
        print("Error en la creacion del registro")
    print("")

def agregar_alumnos_masivo():
    try:#Agregar multiples alumnos a la base de datos, por medio de un archivo de texto, que contiene registros de alumnos
        conexion = sqlite3.connect("alumnos.sqlite")
        cursor = conexion.cursor()
        nombre_archivo = input('Ingrese nombre del archivo: ') #Para capturar errores se recomienda colocar try except
        datos_alumnos = open(nombre_archivo, "r")
        for registro in datos_alumnos:
            linea = registro.split(",")
            cedula = linea[0]
            nombre = linea[1]
            apellido = linea[2]
            sexo = linea[3]
            nro_asignaturas = linea[4]
            promedio = linea[5]
            porc_aprobadas = linea[6] 
            linea2 = registro.split("[") #Se usa otro split para poder guardar la lista de notas correctamente
            notas = "[" + linea2[1].rstrip()
            data = (cedula, nombre, apellido, sexo, nro_asignaturas, promedio, porc_aprobadas, notas,)
            query = "INSERT into Alumnos (cedula, nombre, apellido, sexo, nro_asignaturas, promedio, porc_aprobadas, notas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, data)
            conexion.commit()
        cursor.close()
        datos_alumnos.close()
        print("Alumnos agregados a la base de datos")
    except:
        print("Error al añadir los nuevos registros")
    print("")

def leer_alumno():
    #Se ingresa un numero de cedula al sistema, para mostrar los datos de un alumnos
    conexion = sqlite3.connect("alumnos.sqlite")
    cursor = conexion.cursor()
    cedula_buscar = input("Ingrese cedula: ") #revisar
    query = "SELECT * from Alumnos WHERE cedula = ?"
    resultado = cursor.execute(query, (cedula_buscar,))
    if (resultado):
        for i in resultado:
            print(f"Cedula: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, Promedio: {i[5]}, % Materias aprobadas: {i[6]} %")
    else:
        print(f"No existe alumno, con nro de cedula, {cedula_buscar}")
        cursor.close()
    print("")

def mostrar_alumnos():
    #Se muestran en consola todos los alumnos registrados en el la base de datos
    conexion = sqlite3.connect("alumnos.sqlite")
    cursor = conexion.cursor()
    query = "SELECT * from Alumnos"
    resultado = cursor.execute(query)
    if (resultado):
        print("\n=====Registros Disponibles=====")
        print("\nCedula==Nombre===Apellido==Promedio==% Aprob")
        for i in resultado:
            print("")
            print(f"{i[0]}, {i[1]}, {i[2]}, {i[5]}, {i[6]} %")
    else:
        pass
    print("")

def actualizar_alumno():
    #Se modifican / actualizan los datos de un alumno ya regsitrado en el sistema
    print("")
    conexion = sqlite3.connect("alumnos.sqlite")
    cursor = conexion.cursor()
    cedula = input("Ingrese cedula: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    sexo = input("Ingrese sexo: ")
    nro_asignaturas = input("Ingrese numero de asignaturas: ")
    promedio = input("Ingrese promedio: ")
    porc_aprobadas = input("Ingrese porcentaje de materias aprobadas: ")
    notas = input("Ingrese lista de notas: ")
    data = (nombre, apellido, sexo, nro_asignaturas, promedio, porc_aprobadas, notas, cedula,)
    query = "UPDATE Alumnos set nombre = ?, apellido = ?, sexo = ?, nro_asignaturas = ?, promedio = ?, porc_aprobadas = ?, notas = ? WHERE cedula = ?"
    resultado = cursor.execute(query, data)
    conexion.commit()
    cursor.close()
    if (resultado):
        print(f"Datos del alumno {cedula} actualizados")
    else:
        print("Hubo error en actualizar los datos")
    print("")

def eliminar_alumno():
    #Se elimina un alumno registrado en el sistema, se busca el numero de cedula
    conexion = sqlite3.connect("alumnos.sqlite")
    cursor = conexion.cursor()
    cedula = input("Ingrese cedula del alumno a eliminar: ")
    query = "DELETE from Alumnos where cedula = ?"
    resultado = cursor.execute(query, (cedula,))
    conexion.commit()
    cursor.close()
    if (resultado):
        print(f"Datos del alumno {cedula} eliminados")
    else:
        print("Hubo error en eliminar el alumno")
    print("")

#progama principal
def main():
    #creacion de base de datos y tabla de alumnos, desde 0, si no estan creadas
    conexion = sqlite3.connect('alumnos.sqlite')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos (cedula TEXT, nombre TEXT, apellido TEXT, sexo TEXT, nro_asignaturas INTEGER, promedio REAL, porc_aprobadas REAL, notas TEXT)''')
    cursor.close()
    
    #Ciclo para opciones del crud
    try:
        while (True):
            print("Base de datos de alumnos")
            print("Indique la operacion a realizar:")
            print("1). Agregar alumno(s): ")
            print("2). Leer / Mostrar registros: ")
            print("3). Actualizar datos: ")
            print("4). Eliminar alumno: ")
            print("5). Salir")
            ch = int(input("Seleccione opcion: "))
            if ch == 1:
                print("1). Agregar alumno(s) manualmente")
                print("2). Agregar alumno(s) de forma masiva")
                opcion1 = int(input("Ingresa opcion: "))
                if opcion1 == 1:
                    agregar_alumno()
                elif opcion1 == 2:
                    agregar_alumnos_masivo()
                else:
                    print("Opcion ingresada no valida")
            elif ch == 2:
                print("1). Leer datos de un alumno")
                print("2). Leer todos los alumnos registrados")
                opcion = int(input("Ingresa opcion: "))
                if opcion == 1:
                    leer_alumno()
                elif opcion == 2:
                    mostrar_alumnos()
                else:
                    print("Opcion ingresada no valida")
            elif ch == 3:
                actualizar_alumno()
            elif ch == 4:
                eliminar_alumno()
            elif ch == 5:
                break
            else:
                print("Ingrese opcion valida")
    except:
        print("Error en la base de datos")

if __name__ == "__main__": #Llamado a subprograma principal
    main()