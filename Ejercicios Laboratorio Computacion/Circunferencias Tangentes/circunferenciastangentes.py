
def leer_circunferencias(registro):
    lista_registro = registro.split(",")
    x1 = float(lista_registro[0])
    y1 = float(lista_registro[1])
    r1 = float(lista_registro[2])
    x2 = float(lista_registro[3])
    y2 = float(lista_registro[4])
    r2 = float(lista_registro[5])
    return x1, y1, r1, x2, y2, r2

def ordenar_circunferencias(x1, y1, r1, x2, y2, r2):
    if r2 > r1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1
    return x1, y1, r1, x2, y2, r2

def distancia_centros(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def relacion_tangencial(x1, y1, r1, x2, y2, r2):
    distancia_c1c2 = distancia_centros(x1, y1, x2, y2)
    relacion = 1 #son externas
    if distancia_c1c2 == r1 - r2:
        if (x1 == x2) and (y1 == y2):
            relacion = 4 #son iguales
        else:
            relacion = 2  # internas
    else: #no tangencial
        relacion = 3
    return relacion

def imprimir_circunferencias(archivo, x1, y1, r1, x2, y2, r2, relacion):
    archivo.write("[(%.2f , %.2f), %.2f] [(%.2f , %.2f), %.2f] %d \n" %(x1, y1, r1, x2, y2, r2, relacion))

def main():
    #apertura de archivos
    circunferencias = open("circunferencias.txt", "r")
    resultados = open("resultados_circunferencias.txt", "w")
    bandera = 0

    for registro in circunferencias:
        x1, y1, r1, x2, y2, r2 = leer_circunferencias(registro)
        x1, y1, r1, x2, y2, r2 = ordenar_circunferencias(x1, y1, r1, x2, y2, r2)
        relacion = relacion_tangencial(x1, y1, r1, x2, y2, r2)
        imprimir_circunferencias(resultados, x1, y1, r1, x2, y2, r2, relacion)

        if bandera == 0:
            bandera = 1
            x_mayor = x1
            y_mayor = y1
            r_mayor = r1
        elif r1 > r_mayor:
            r_mayor = r1
            x_mayor = x1
            y_mayor = y1

    print("la circunferencia con mayor radio es: ", x_mayor, y_mayor, r_mayor)           
    circunferencias.close()
    resultados.close()

    # (1:externa, 2: interna, 3: No tangencial y 4: Son iguales)    
    #Tangente Extena: Dc1c2 = r1 + r2
    #Tangente Interna: Dc1c2 = r1 - r2
    #No Tangentes: Dc1c2 != r1-r2 y Dc1c2 != r1+r2

if __name__ == "__main__":
    main()

    