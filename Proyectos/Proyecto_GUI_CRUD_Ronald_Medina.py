# Proyecto #: Agenda de Trabajadores, Asignatura: Programacion Basica
# Proposito / Enunciado: Crear una aplicacion de interzaz grafico de usuario (GUI), donde se muestra una base de datos de empleados de una empresa.
# La base de datos esta elaborada en sqlite3. 
# Por medio de la aplicacion se pueden realizar las siguientes operaciones:
# Crear y /o conectar a la base de datos, Eliminar la base de datos, Mostrar los empleados registrados,
# Modificar / Actualizar los datos de un empleado, Agregar un nuevo empleado a la base de datos, eliminar un empleado de la base de datos.
# Todas estas operaciones se realizan por medio de la GUI, realizando los cambios correspondientes en la base de datos.
# Los campos que posee cada empleado son los siguientes: ID (automatico), Nombre, Cargo y Salario
# Autor: Ronald Medina 
# Fecha de elaboracion: 03 / 02 / 2023


# Importacion de librerias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

# Desarrollo de la interfaz grafica
root = Tk()
root.title("Aplicacion CRUD, Base de datos de Empleados")
root.geometry("600x350")

# Variables de manejo de informacion
mi_id = StringVar()
mi_nombre = StringVar()
mi_cargo = StringVar()
mi_salario = StringVar()


# Creacion de la tabla variable tipo arbol ttk
tree = ttk.Treeview(height=10, columns=('#0','#1','#2')) #Arbol de datos
tree.place(x = 0, y = 130)
tree.column('#0', width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre del Empleado", anchor=CENTER)
tree.heading('#2', text="Cargo", anchor=CENTER)
tree.column('#3',width=100)
tree.heading('#3', text="Salario", anchor=CENTER)


# Funciones de BBDD y auxiliares
def conexion_BBDD():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    try:
        mi_cursor.execute("""
        CREATE TABLE empleado (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL,
        CARGO VARCHAR(50) NOT NULL,
        SALARIO INT NOT NULL)
        """)
        messagebox.showinfo("CONEXION", "Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "Conexion exitosa con la base de datos")


def eliminar_BBDD():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente, Desea continuar?", title="Advertencia"):
        mi_cursor.execute("DROP TABLE empleado")
    else:
        pass


def salir_aplicacion():
    valor = messagebox.askquestion("Salir", "Esta seguro que desea salir de la aplicacion?")
    if valor == "yes": 
        root.destroy()


def limpiar_campos():
    mi_id.set("")
    mi_nombre.set("")
    mi_cargo.set("")
    mi_salario.set("")


def mensaje():
    acerca = """
    Aplicacion CRUD, "Empleados"
    Elaborado: Ing. Ronald Medina
    Fecha: 03/03/2023
    Version 1.0
    GUI Python Tkinter
    """
    messagebox.showinfo(title="INFORMACION", message=acerca)


def seleccionar_datos_click(event):
    item = tree.identify("item", event.x, event.y)
    mi_id.set(tree.item(item,"text"))
    mi_nombre.set(tree.item(item, "values")[0])
    mi_cargo.set(tree.item(item, "values")[1])
    mi_salario.set(tree.item(item, "values")[2])

tree.bind("<Double-1>", seleccionar_datos_click)


# Funciones CRUD
def crear():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    try:
        datos = mi_nombre.get(), mi_cargo.get(), mi_salario.get() #Preguntar al pofesor como hacer para no crear usuarios con campos vacios
        mi_cursor.execute("INSERT INTO empleado VALUES(NULL, ?, ?, ?)", (datos))
        mi_conexion.commit()
    except:
        messagebox.showwarning(title="ADVERTENCIA", message="Error al crear registro, verifique conexion con BBDD")
        pass
    limpiar_campos()
    mostrar()


def mostrar():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        mi_cursor.execute("SELECT * FROM empleado")
        for row in mi_cursor: # Preguntar al profe para mostar los contactos ID de forma ascedente (Mas antiguo al mas reciente)
            tree.insert("", 0 ,text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass


def actualizar():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    try:
        datos = mi_nombre.get(), mi_cargo.get(), mi_salario.get()
        mi_cursor.execute("UPDATE empleado SET NOMBRE = ?, CARGO =?, SALARIO =? WHERE ID =" + mi_id.get(), (datos))
        mi_conexion.commit()
    except:
        messagebox.showwarning(title="ADVERTENCIA", message="Error al actualizar registro, verifique conexion con BBDD")
        pass
    limpiar_campos()
    mostrar()
 

def borrar():
    mi_conexion = sqlite3.connect("base.sqlite")
    mi_cursor = mi_conexion.cursor()
    try:
        if messagebox.askyesno(message="Desea eliminar el registro?", title="ADVERTENCIA"):
            mi_cursor.execute("DELETE FROM empleado WHERE ID="+mi_id.get())
            mi_conexion.commit()
    except:
        messagebox.showwarning(title="ADVERTENCIA", message="Error al eliminar registro, verifique conexion con BBDD")
        pass
    limpiar_campos()
    mostrar()


# Elementos de la configuracion de la ventana
# Creacion de menus
menu_bar = Menu(root)

menu_base_datos = Menu(menu_bar, tearoff=0)
menu_base_datos.add_command(label="Crear / Conectar Base de Datos", command=conexion_BBDD)
menu_base_datos.add_command(label="Eliminar Base de Datos", command=eliminar_BBDD)
menu_base_datos.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Inicio", menu=menu_base_datos)

menu_ayuda = Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Reset de campos", command=limpiar_campos)
menu_ayuda.add_command(label="Acerca de...", command=mensaje)
menu_bar.add_cascade(label="Ayuda",menu=menu_ayuda)

# Entrada de datos, recolecta los registros que van a ser tratados en la aplicacion
id_entrada = Entry(root, textvariable= mi_id)

# Creacion de cajas de textos y etiquetas
nombre_entrada = Entry(root, textvariable= mi_nombre, width=50)
nombre_entrada.place(x=100, y=10)
nombre_label = Label(root, text="Nombre")
nombre_label.place(x=50, y=10)

cargo_entrada = Entry(root, textvariable= mi_cargo)
cargo_entrada.place(x=100, y=40)
cargo_label = Label(root, text="Cargo")
cargo_label.place(x=50, y=40)

salario_entrada = Entry(root, textvariable= mi_salario, width=10)
salario_entrada.place(x=320, y=40)
salario_label = Label(root, text="Salario")
salario_label.place(x=280, y=40)

moneda_label = Label(root, text="$(US)")
moneda_label.place(x=380, y=40)

# Creacion de botones
boton_crear = Button(root, text="Crear Registro", command=crear)
boton_crear.place(x=50, y=90)

boton_actualizar = Button(root, text="Modificar Registro", command=actualizar)
boton_actualizar.place(x=180, y=90)

boton_mostrar = Button(root, text="Mostrar Empleados", command=mostrar)
boton_mostrar.place(x=320, y=90)

boton_eliminar = Button(root, text="Eliminar Registro", bg= "red", command=borrar)
boton_eliminar.place(x=450, y=90)

root.config(menu=menu_bar)

#Instrucion para ejecutar aplicacion de escritorio
root.mainloop()