def leer_juego(registro):
    linea = registro.split(",")
    visitante = linea[0]
    local = linea[1]
    anotadas_visitante = int(linea[2])
    anotadas_local = int(linea[3])
    innings = float(linea[4])
    errores = int(linea[5])
    return visitante, local, anotadas_visitante, anotadas_local, innings, errores 

def resultado_juego(visitante, local, anotadas_visitante, anotadas_local):
    if anotadas_local > anotadas_visitante:
        ganador = local
        carreras_permitidas_ganador = anotadas_visitante
        perdedor = visitante
        carreras_permitidas_perdedor = anotadas_local
    else:
        ganador = visitante
        carreras_permitidas_ganador = anotadas_local
        perdedor = local
        carreras_permitidas_perdedor = anotadas_visitante
    return ganador, carreras_permitidas_ganador, perdedor, carreras_permitidas_perdedor

def imprimir_equipo(archivo, equipo, ganados, perdidos, porc_victoria, anotadas, permitidas, entradas):
    archivo.write(f'{equipo}, {ganados}, {perdidos}, {porc_victoria} %, {anotadas}, {permitidas}, {entradas} \n')

def main():
    datos_serie_caribe23 = open("serie2023.txt", "r")
    resultados = open("resultados_serie2023.txt", "w")
    
    juego_ven, juego_mex, juego_cuba = 0, 0, 0
    ganados_ven, ganados_mex, ganados_cuba = 0, 0, 0
    entradas_ven, entradas_cuba, entradas_mex = 0, 0, 0
    permitidas_ven, permitidas_mex, permitidas_cuba = 0, 0, 0
    anotadas_ven, anotadas_mex, anotadas_cuba = 0, 0, 0
    bandera = 0
    equipo_ganador = ""
    victorias_ganador = 0
    anotadas_ganador = 0

    for juego in datos_serie_caribe23:
        visitante, local, anotadas_visitante, anotadas_local, innings, errores = leer_juego(juego)
        ganador, carreras_permitidas_ganador, perdedor, carreras_permitidas_perdedor = resultado_juego(visitante, local, anotadas_visitante, anotadas_local)
        #print(ganador, carreras_permitidas_ganador, perdedor, carreras_permitidas_perdedor)
        if ganador == "venezuela" and perdedor == "cuba":
            juego_ven += 1
            juego_cuba += 1
            ganados_ven += 1
            permitidas_ven += carreras_permitidas_ganador
            permitidas_cuba += carreras_permitidas_perdedor
            anotadas_ven += carreras_permitidas_perdedor
            anotadas_cuba += carreras_permitidas_ganador
            entradas_ven += innings
            entradas_cuba += innings
        elif ganador == "venezuela" and perdedor == "mexico": 
            juego_ven += 1
            juego_mex += 1
            ganados_ven += 1
            permitidas_ven += carreras_permitidas_ganador
            permitidas_mex += carreras_permitidas_perdedor
            anotadas_ven += carreras_permitidas_perdedor
            anotadas_mex += carreras_permitidas_ganador
            entradas_ven += innings
            entradas_mex += innings
        elif ganador == "cuba" and perdedor == "mexico":
            juego_cuba += 1
            juego_mex +=1
            ganados_cuba += 1 
            permitidas_cuba += carreras_permitidas_ganador
            permitidas_mex += carreras_permitidas_perdedor
            anotadas_cuba += carreras_permitidas_perdedor
            anotadas_mex += carreras_permitidas_ganador
            entradas_cuba += innings
            entradas_mex += innings
        elif ganador == "cuba" and perdedor == "venezuela":
            juego_cuba += 1
            juego_ven +=1
            ganados_cuba += 1 
            permitidas_cuba += carreras_permitidas_ganador
            permitidas_ven += carreras_permitidas_perdedor
            anotadas_cuba += carreras_permitidas_perdedor
            anotadas_ven += carreras_permitidas_ganador
            entradas_ven += innings
            entradas_mex += innings
        elif ganador == "mexico" and perdedor == "cuba":
            juego_mex += 1
            juego_cuba += 1
            ganados_mex += 1
            permitidas_mex += carreras_permitidas_ganador
            permitidas_cuba += carreras_permitidas_perdedor
            anotadas_mex += carreras_permitidas_perdedor
            anotadas_cuba += carreras_permitidas_ganador
            entradas_mex += innings
            entradas_cuba += innings
        else: #gano mexico perdio vene
            juego_mex += 1
            juego_ven += 1
            ganados_mex += 1
            permitidas_mex += carreras_permitidas_ganador
            permitidas_ven += carreras_permitidas_perdedor
            anotadas_mex += carreras_permitidas_perdedor
            anotadas_ven += carreras_permitidas_ganador
            entradas_mex += innings
            entradas_ven += innings
                   
    imprimir_equipo(resultados,"venezuela", ganados_ven, (juego_ven - ganados_ven), round((ganados_ven / juego_ven) * 100, 2), anotadas_ven, permitidas_ven, entradas_ven)
    imprimir_equipo(resultados,"mexico", ganados_mex, (juego_mex - ganados_mex), round((ganados_mex / juego_mex) * 100, 2), anotadas_mex, permitidas_mex, entradas_mex)
    imprimir_equipo(resultados,"cuba", ganados_cuba, (juego_cuba - ganados_cuba), round((ganados_cuba / juego_cuba) * 100, 2), anotadas_cuba, permitidas_cuba, entradas_cuba)

    resultados.close()
    ver_resultados = open("resultados_serie2023.txt", "r")  

    for equipo in ver_resultados:
        linea = equipo.split(",")
        equipo = linea[0]
        ganados= linea[1]
        anotadas = linea[4]
        if bandera == 0:
            bandera = 1
            equipo_ganador = equipo
            victorias_ganador = ganados
            anotadas_ganador = anotadas
        elif ganados > victorias_ganador:
            victorias_ganador = ganados
            equipo_ganador = equipo
            anotadas_ganador = anotadas
    
    print("El equipo con mayor victorias es", equipo_ganador, "con", victorias_ganador, "victorias, y anoto en total", anotadas_ganador, "carreras")
    datos_serie_caribe23.close()
    ver_resultados.close()

if __name__ == "__main__":
    main()