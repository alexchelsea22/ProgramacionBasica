# Tarea # 2: Programacion Basica
# Proposito / Enunciado: Crear un lista de contactos que permita:
# agregar un contacto, modificar / actualizar datos de un contacto,
# eliminar un contacto de la lista y mostrar la lista de contactos.
# Los datos de un contacto son : nombre, apellido, telefono, email
# Autor: Ronald Medina 
# Fecha de elaboracion: 11 / 02 / 2023

# Contacto iniciales en la libreta de contacto, un diccionario "contactos",
# donde la llave es el indice, y el valor es un diccionario anidado con la info de cada contacto
contactos = {
    1 : {
        "nombre" : "Ronald",
		"apellido" : "Medina",
        "telefono" : "1329387",
        "email" : "rmedina@gmail.com"
    },
    2 : {
        "nombre" : "Alex",
		"apellido": "Chelsea",
        "telefono" : "2034988",
        "email" : "achelsea@yahoo.com"
    },
    3 : {
        "nombre" : "Ana",
		"apellido" : "Lopez",
        "telefono" : "4654523",
        "email" : "alopez@hotmail.com"
    }
}


# Funcion para mostrar en pantalla las opciones de la libreta
def mostrarMenu():
	print("Libreta de contactos: Indique la operacion a realizar:")
	print("1. Ver contactos")
	print("2. Actualizar / Modificar un contacto")
	print("3. Añadir un contacto")
	print("4. Eliminar un contacto")
	print("5. Salir")
	seleccionarMenu()


# Funcion que toma el valor inresado por el usuario para realizar la operacion elegida
def seleccionarMenu():
    repetir = True
    while repetir == True:
        try:
            operacion = int(input("Escoge [1-5]: "))
        except ValueError:
            print("Ingrese un numero:")
        # Se inicializa en 0 la operacion para evitar el error
            operacion = 0
        if operacion > 0 and operacion < 6: repetir = False
        if operacion == 1:
            mostrarContactos()
            mostrarMenu()
        elif operacion == 2:
            print("\n============================")
            print("Cambiar / Modificar contacto")
            print("============================")
            actualizarContacto()
            mostrarMenu()
        elif operacion == 3:
            print("\n=================")
            print("Añadir un contacto")
            print("==================")
            agregarContacto()
            mostrarMenu()
        elif operacion == 4:
            eliminarContacto()
            mostrarMenu()
        elif operacion == 5:
            print("Programa Finalizado")
            break
        else: 
            print("Opcion no disponible")


# Funcion que muestra en pantalla la lista de contactos de la libreta de contactos
def mostrarContactos():
    # Numeracion de los contactos
    num = 1
    print("====================================================================================")
    print("|No.| Nombre         | Apelllido        | Telefono         | Email                 |")
    print("====================================================================================")
    for contacto in contactos.values():
        # Formato con alineacion a la izquierda y dar espacio
        print("|{no} .| {nombre:<15}  | {apellido:<15}  | {telefono:<15}  | {email:<25} |"
        .format(no = num, nombre = contacto["nombre"], apellido = contacto["apellido"],
                telefono = contacto["telefono"], email = contacto["email"]))
        num += 1
    print("====================================================================================")
    # Nota: tiene detalles de impresion, preguntar al profesor


# Funcion que añade un contacto nuevo a la libreta de contactos
def agregarContacto():
    # Con la lista orden_contacto, se obtiene la ultima llave de contactos y se incremente en 1
    orden_contactos = list(contactos.keys())[-1] + 1
    # Se solicita al usuario, ingresar los datos del nuevo contacto que se va agregar a la libreta
    while True:
        # Se coloca un try / excepcion para asegurar valores validos
        try:
            nombre = str(input("Ingrese nombre del contacto: "))
            apellido = str(input("Ingrese apellido del contacto: "))
            telefono = str(input("Ingrese numero de telefono: "))
            email = str(input("Ingrese email: "))
            # Se añade los campos del usuario nuevo, al diccionario contactos
            contactos[orden_contactos] = {
                "nombre" : "{}". format(nombre),
                "apellido" : "{}". format(apellido),
                "telefono" : "{}". format(telefono),
                "email" : "{}".format(email)
            }
            print("Los datos de " + nombre + " fueron agregados exitosamente!\n")
            break
        except ValueError:
            print("Valores no validos, Por favor ingrese un formato correcto.\n")
            break


# Funcion que actualiza los datos, de un contacto
def actualizarContacto():
    ya_actualizado = False
    mostrarContactos()
    # Se solicita al usuario, ingresar el nombre del usuario que se va a actualizar / modificar
    nombre_previo = str(input("Ingrese nombre del contacto que deseas cambiar: "))
    # Se verifica el nombre
    for contacto in contactos.values():
        if nombre_previo in contacto.values():
            print("Datos de " + nombre_previo + " encontrados")
            # Se coloca un try / excepcion para asegurar valores validos
            try:
                nombre_nuevo = str(input("Ingrese nuevo nombre del contacto: "))
                apellido_nuevo = str(input("Ingrese nuevo apellido del contacto: "))
                telefono_nuevo = str(input("Ingrese telefono nuevo: "))
                email_nuevo = str(input("Ingrese email nuevo: "))
                # Se actualiza los datos del contacto
                contacto.update({"nombre" : "{}". format(nombre_nuevo)})
                contacto.update({"apellido" : "{}". format(apellido_nuevo)})
                contacto.update({"telefono" : "{}". format(telefono_nuevo)})
                contacto.update({"email" : "{}". format(email_nuevo)})
                ya_actualizado = True
                print("Los datos de '{}' han sido cambiados a '{}'.\n".format(nombre_previo, nombre_nuevo))
                
            except ValueError:
                print("Valores no validos, error de formato, por favor ingrese un numero correcto.") 

    if ya_actualizado == False:
        #Si se ingresa un valor que no esta en el diccionario
        print("Datos no encontrados. Por favor ingrese un nombre correcto\n")
        mostrarMenu()


# Esta funcion elimina un contacto de la libreta de contacto, se solicita un nombre 
def eliminarContacto():
    ya_borrado = False
    mostrarContactos()
    nombre = str(input("Ingrese nombre del contacto que desea eliminar: "))
    for llave_contacto, info_contacto in list(contactos.items()):
        if info_contacto["nombre"] == nombre:
            del contactos[llave_contacto]
            mostrarContactos()
            print("Los datos de '{}' han sido borrados exitosamente!\n".format(nombre))
            ya_borrado = True
    if ya_borrado == False: print("Datos no encontrados!\n")

# inicio de programa
mostrarMenu()
