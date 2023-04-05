from math import sqrt

def es_igual(a, b, tol):
    return abs(a - b) < tol

def tipo_triangulo(d12, d13, d23):
    tipo = "isoceles"
    if es_igual (d12, d13, 0.003) and es_igual(d12, d23, 0.003):
        tipo = "equilatero"
    elif (d12 != d13) and (d12 != d23) and (d13 != d23):
        tipo = "escaleno"
    return tipo

def leer_linea(archivo):
    datos = archivo.readline().split(",")
    x1 = float(datos[0])
    y1 = float(datos[1])
    x2 = float(datos[2])
    y2 = float(datos[3])
    x3 = float(datos[4])
    y3 = float(datos[5])
    return x1, y1, x2, y2, x3, y3

def distancia_puntos(x1, y1, x2 ,y2):
    return sqrt( (x2 - x1) ** 2 + (y2 - y1)**2)

def distancias(x1,  y1,  x2,  y2,  x3 , y3):
    d12 = distancia_puntos(x1, y1, x2 ,y2)
    d13 = distancia_puntos(x1, y1, x3 ,y3)
    d23 = distancia_puntos(x2, y2, x3 ,y3)
    return d12, d13, d23

def area_triangulo(d12, d13, d23):
    s = (d12 + d13 + d23) / 2
    return sqrt(s * (s -d12) * (s -d13) * (s -d23))

def verificar_triangulo(d12, d13, d23):
    return d12 < (d13 +d23) and d13 < (d13 + d23) and d23 < (d12 + d13)

def imprimir_triangulo(archivo, x1, y1, x2, y2, x3, y3, tipo, area):
    archivo.write("(%.2f , %.2f) (%.2f , %.2f) (%.2f , %.2f) %s %.2f  \n" %(x1, y1, x2, y2, x3, y3, tipo, area))

def main():
    datos = open('posibles.txt', 'r')
    respuestas = open('triangulos.txt', 'w')
    nro_triangulos = int(datos.readline())
   
    for _ in range(nro_triangulos):
        tipo = ""
        x1, y1, x2, y2, x3 ,y3 = leer_linea(datos)
        d12, d13, d23 =   distancias(x1,  y1,  x2,  y2,  x3 , y3)
        if verificar_triangulo(d12, d13, d23):
            area = area_triangulo(d12, d13, d23)
            tipo = tipo_triangulo(d12, d13, d23)
            imprimir_triangulo(respuestas, x1, y1, x2, y2, x3, y3, tipo, area)
        else:
            print("no se puede formar un triangulo")
            
    datos.close()
    respuestas.close()
 
if __name__ == "__main__":
    main()
    
    
    
        