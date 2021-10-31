"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import orderedmapstructure as om
from tabulate import tabulate
from DISClib.DataStructures import mapentry as me
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Crear el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos por su duración")
    print("5- Contar los avistamientos en un rango de tiempo")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos en una zona geográfica")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Creando catálogo...")
        catalog = controller.initCatalog()
        print("Catálogo creado con éxito")

    elif int(inputs[0]) == 2:
        print("Cargando información en el catálogo...")
        controller.loadData(catalog)
        lista = catalog['avistamientos']
        print('Se han cargado '+str(lt.size(lista))+" avistamientos")

    elif int(inputs[0])==3:
        ciudad = input('Ingrese la ciudad que desea consultar: ')
        peso = om.size(catalog['ciudades'])
        print("Hay "+ str(peso)+ " ciudades que tienen avistamientos de UFOs")
        listaCiudad = controller.darAvistamientosCiudad(catalog, ciudad)
        if listaCiudad != False:
            info = controller.darInfoReq1(listaCiudad)
            print('Hay un total de '+str(lt.size(listaCiudad))+' avistamientos en '+ciudad)
            print('Los primeros y últimos 3 avistamientos en '+ciudad+ ' son:')
            print(tabulate(info, headers=['datetime', 'city','country','duration (seconds)','shape'], tablefmt='fancy_grid'))
        else:
            print('Esta ciudad no se encuentra en la base de datos')
    
    elif int(inputs[0])==4:
        inf = input('Ingrese la duración mínima del avistamiento: ')
        try:
            inf = float(inf)
            sup = input('Ingrese la duración máxima del avistamiento: ')
            sup = float(sup)
            duracionMaxima = om.maxKey(catalog['duracion'])
            valor = om.get(catalog['duracion'], duracionMaxima)
            lista = me.getValue(valor)
            print('Hay '+str(om.size(catalog['duracion']))+' duraciones diferentes para los avistamientos')
            print('La duración máxima de los avistamientos es: ')
            datos=[[duracionMaxima, lt.size(lista)]]
            print(tabulate(datos, headers=['duration (seconds)', 'count'], tablefmt='fancy_grid'))
            mapa = controller.darMapaRangoDuracion(catalog, inf, sup)
            listaDuraciones = lt.newList('ARRAY_LIST')
            listaDuraciones = controller.darListaDuraciones(mapa['root'], listaDuraciones)
            info = controller.darInfoReq2(listaDuraciones)
            print('Hay un total de '+str(lt.size(listaDuraciones))+' avistamientos entre '+str(inf)+' y '+str(sup)+' segundos.')
            print('Los primeros y últimos 3 avistamientos en el rango de duración son:')
            print(tabulate(info, headers=['datetime', 'city','country','duration (seconds)','shape'], tablefmt='fancy_grid'))
        except ValueError:
            print('La última duración ingresada es inválida')

    elif int(inputs[0])==6:
        inicio=input("Ingrese el año inicial de compra en formato AAAA-MM-DD: ")
        formato = inicio.split('-')
        if (len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2 
        or formato[0].isnumeric() == False or formato[1].isnumeric() == False or formato[2].isnumeric() == False):
            print('Ha ingresado una fecha inicial inválida')
        else:
            fin = input('Ingrese el año final de compra en formato AAAA-MM-DD: ')
            formato = fin.split('-')
            if (len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2 
            or formato[0].isnumeric() == False or formato[1].isnumeric() == False or formato[2].isnumeric() == False or inicio > fin):
                print('Ha ingresado una fecha final inválida')
            else: 
                fechaMinima = om.minKey(catalog['fechas'])
                valor = om.get(catalog['fechas'], fechaMinima)
                lista = me.getValue(valor)
                print('Hay '+str(om.size(catalog['fechas']))+' fechas diferentes para los avistamientos')
                print('Los avistamientos más viejos ocurrieron en: ')
                datos=[[fechaMinima, lt.size(lista)]]
                print(tabulate(datos, headers=['date', 'count'], tablefmt='fancy_grid'))
                mapa = controller.darMapaRangoFechas(catalog, inicio, fin)
                listaFechas = lt.newList('ARRAY_LIST')
                listaFechas = controller.darListaFechas(mapa['root'], listaFechas)
                info = controller.darInfoReq2(listaFechas)
                print('Hay un total de '+str(lt.size(listaFechas))+' avistamientos entre '+inicio+' y '+fin)
                print('Los primeros y últimos 3 avistamientos en el rango son:')
                print(tabulate(info, headers=['datetime', 'city','country','duration (seconds)','shape'], tablefmt='fancy_grid'))
            

        

    else:
        sys.exit(0)
sys.exit(0)
