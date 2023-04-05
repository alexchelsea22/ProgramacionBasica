from math import ceil

def calculo_cajas(area, baldosa_cm2, baldosas_x_caja):
    cajas = ceil(area / ((baldosa_cm2 / 10000) * baldosas_x_caja))
    return cajas

def leer_cliente(registro):
    linea = registro.split(',')
    codigo_cliente = linea[0]
    area = float(linea[1])
    tipo_baldosa = int(linea[2])
    return codigo_cliente, area, tipo_baldosa

def imprimir(archivo, cliente, cajas, monto): #imprime una linea
    archivo.write(f'Cliente = {cliente}, Nro cajas = {str(cajas)}, Costo trabajo = {monto}\n')
     
def main():
    clientes = open("clientes.txt", "r")
    resultado = open("resultadobaldosa.txt", "w")
    #contenido = clientes.readlines()
    cont_normal, cont_extra = 0, 0
    cliente_menor = ""
    area_menor = 0
    bandera = 0
    
    for registro in clientes:
        cliente, area, tipo_baldosa = leer_cliente(registro)
        if tipo_baldosa == 0: #baldosa normal  baldosa 25 cm2, baldosas x caja 20, pu caja 45
            cont_normal += 1
            nro_cajas = calculo_cajas(area, 25, 20)
            costo = round(nro_cajas * 45, 2)
            imprimir(resultado, cliente, nro_cajas, costo)
        else: #baldosa extra baldosa 45 cm2, baldosas x caja 12, pu caja 56
            cont_extra += 1
            nro_cajas = calculo_cajas(area, 45, 12)
            costo = round(nro_cajas * 56, 2)
            imprimir(resultado, cliente, nro_cajas, costo)

        if bandera == 0:
            bandera = 1
            area_menor = area
            cliente_menor = cliente
        elif area_menor > area:
            area_menor = area
            cliente_menor = cliente

    porcentaje_normal = round((cont_normal / (cont_normal + cont_extra)) * 100, 2)
    print("Porcentaje de clientes baldosa normal: ", porcentaje_normal, "%")
    print("El cliente con el area menor es", cliente_menor, "con un area ", area_menor, "m2")

    clientes.close()
    resultado.close()

if __name__ == "__main__":
    main()
