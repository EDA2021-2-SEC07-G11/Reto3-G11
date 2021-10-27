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
        altura = om.height(catalog['ciudades'])
        peso = om.size(catalog['ciudades'])
        print("El mapa de ciudades contiene "+ str(peso)+ " ciudades")
        print("La altura de este mapa es "+str(altura))

    else:
        sys.exit(0)
sys.exit(0)
