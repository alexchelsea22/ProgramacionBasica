def convertir_a_segundos(hora, minutos, segundos):
    hora_en_seg = 3600 * hora
    min_en_seg = minutos * 60
    return hora_en_seg + min_en_seg + segundos

def tiempo_laborado(hora_entrada, min_entrada, seg_entrada, hora_salida, min_salida, seg_salida):
    total_seg_lab = convertir_a_segundos(hora_salida, min_salida, seg_salida)  - convertir_a_segundos(hora_entrada, min_entrada, seg_entrada) - 3600
    aux = total_seg_lab
    hora_laborado = aux // 3600
    aux = aux % 3600
    min_laborado = aux // 60
    aux = aux % 60
    seg_laborado = aux 
    return hora_laborado, min_laborado, seg_laborado

def leer_tiempo(registro):
    linea = registro.split(",")
    cedula = linea[0]
    sexo = linea[1]
    hora_entrada = int(linea[2])
    min_entrada = int(linea[3])
    seg_entrada = int(linea[4])
    hora_salida = int(linea[5])
    min_salida = int(linea[6])
    seg_salida = int(linea[7])
    return cedula, sexo, hora_entrada, min_entrada, seg_entrada, hora_salida, min_salida, seg_salida

def imprimir_empleado(archivo, cedula, hora_laborado, min_laborado, seg_laborado):
    archivo.write(f'{cedula}, [{hora_laborado}:{min_laborado}:{seg_laborado}] \n')
    
def main():

    tiempos_laborales = open("asistencia.txt", "r")
    resultados = open("tiempos_resultados.txt", "w")
    #trabajadores = len(resultados)
    menor_8_h, chicas, cont_total = 0, 0, 0
    prom_chica_hr = 0
    bandera = 0 
    chico_menor = ""
    t_minimo_seg = 0
    horas_chicas = 0
    hora_minimo, min_minimo, seg_minimo = 0, 0, 0
    for trabajador in tiempos_laborales:
        cedula, sexo, hora_entrada, min_entrada, seg_entrada, hora_salida, min_salida, seg_salida = leer_tiempo(trabajador)
        hora_laborado, min_laborado, seg_laborado = tiempo_laborado(hora_entrada, min_entrada, seg_entrada, hora_salida, min_salida, seg_salida)
        #print(hora_laborado, min_laborado, seg_laborado)
        imprimir_empleado(resultados, cedula, hora_laborado, min_laborado, seg_laborado)
        if sexo == "F":
            horas_chicas += hora_laborado
            chicas += 1
        else:
            if bandera == 0:
                bandera = 1
                chico_menor = cedula
                hora_minimo = hora_laborado
                min_minimo = min_laborado
                seg_minimo = seg_laborado
                t_minimo_seg = convertir_a_segundos(hora_laborado, min_laborado, seg_laborado)
            elif convertir_a_segundos(hora_laborado, min_laborado, seg_laborado) < t_minimo_seg:
                chico_menor = cedula
                t_minimo_seg = convertir_a_segundos(hora_laborado, min_laborado, seg_laborado)
                hora_minimo = hora_laborado
                min_minimo = min_laborado
                seg_minimo = seg_laborado

        if hora_laborado <= 7:
           menor_8_h += 1
        cont_total += 1 
    print("% empleados < 8 hr:", round((menor_8_h / cont_total) * 100, 2), "%")
    print("Hr promedio de trabajo - Mujeres", round(horas_chicas / chicas, 2))
    print("Hombre menor tiempo minimo",chico_menor,",",hora_minimo, ":", min_minimo, ":", seg_minimo)
    #print("nro chicas", chicas, "nro < 8", menor_8_h, "chico tiempo menor", chico_menor, "tiempo menor", t_minimo_seg, "horas chicas", horas_chicas, "todos", cont_total)
    tiempos_laborales.close()
    resultados.close()
main()