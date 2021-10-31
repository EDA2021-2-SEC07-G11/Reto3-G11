"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import orderedmapstructure as om
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'ciudades': None, 'avistamientos' : None, 'duracion' : None
                }
    catalog['ciudades'] = om.newMap(omaptype='RBT',comparefunction=compareCities)
    catalog['duracion'] = om.newMap(omaptype='RBT',comparefunction=compareDuration)
    catalog['avistamientos'] = lt.newList("ARRAY_LIST")
    return catalog

# Funciones para agregar informacion al catalogo

def agregarAvistamiento(catalog, avistamiento):
    avistamientos = catalog['avistamientos']
    lt.addLast(avistamientos,avistamiento)
    agregarCiudad(catalog, avistamiento)
    agregarDuracion(catalog, avistamiento)
    

def agregarCiudad(catalog, avistamiento):
    ciudad = avistamiento['city']
    mapa = catalog['ciudades']
    if om.contains(mapa, ciudad):
        valor = om.get(mapa, ciudad)
        entrada = me.getValue(valor)
        lt.addLast(entrada, avistamiento)
    else:
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, avistamiento)
        om.put(mapa, ciudad, lista)

def agregarDuracion(catalog, avistamiento):
    duracion = float(avistamiento['duration (seconds)'])
    mapa = catalog['duracion']
    if om.contains(mapa, duracion):
        valor = om.get(mapa, duracion)
        entrada = me.getValue(valor)
        lt.addLast(entrada, avistamiento)
    else:
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, avistamiento)
        om.put(mapa, duracion, lista)


# Funciones para creacion de datos



# Funciones de consulta

def darAvistamientosCiudad(catalog, ciudad):
    mapa = catalog['ciudades']
    if om.contains(mapa, ciudad):
        valor = om.get(mapa, ciudad)
        return me.getValue(valor)
    else:
        return False

def infoReq1(lista):
    n = lt.size(lista)
    lista = merge.sort(lista, cmpDates)
    datos = []
    if n >= 7:
        k = 1
        while k <4:
            ufo = lt.getElement(lista, k)
            datos.append(infoUFOReq1(ufo))
            k +=1
        k = n-2
        while k <= n:
            ufo = lt.getElement(lista, k)
            datos.append(infoUFOReq1(ufo))
            k +=1
    else:
        for ufo in lt.iterator(lista):
            datos.append(infoUFOReq1(ufo))
    return datos

def infoReq2(lista):
    n = lt.size(lista)
    datos = []
    if n >= 7:
        k = 1
        while k <4:
            ufo = lt.getElement(lista, k)
            datos.append(infoUFOReq1(ufo))
            k +=1
        k = n-2
        while k <= n:
            ufo = lt.getElement(lista, k)
            datos.append(infoUFOReq1(ufo))
            k +=1
    else:
        for ufo in lt.iterator(lista):
            datos.append(infoUFOReq1(ufo))
    return datos


def infoUFOReq1(ufo):
    return ufo['datetime'], ufo['city'], ufo['country'], ufo['duration (seconds)'], ufo['shape']

def darAvistamientosDuraciones(catalog, inf, sup):
    duraciones = catalog['duracion']
    mapa = om.newMap(omaptype='RBT',comparefunction=compareDuration)
    return darDuracion(duraciones['root'], inf, sup, mapa)

def darDuracion(duracion, inf, sup, mapa):
    if duracion['key'] < inf:
        if duracion['right'] != None:
            mapa = darDuracion(duracion['right'], inf, sup, mapa)
    elif duracion['key'] > sup:
        if duracion['left'] != None:
            mapa = darDuracion(duracion['left'], inf, sup, mapa)
    else:
        if duracion['left'] != None:
            mapa = darDuracion(duracion['left'],inf,sup,mapa)
        
        om.put(mapa, duracion['key'], duracion['value'])

        if duracion['right'] != None:
            mapa = darDuracion(duracion['right'],inf,sup,mapa)

    return mapa

def listaDuraciones(raiz, lista):
    if(raiz['left'] != None):
        lista = listaDuraciones(raiz['left'], lista)
    
    valor = raiz['value']
    for ufo in lt.iterator(valor):
        lt.addLast(lista, ufo)

    if(raiz['right'] != None):
        lista = listaDuraciones(raiz['right'], lista)
    
    return lista
    







    
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareCities(c1, c2):
    if c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    else:
        return 0

def compareDuration(d1, d2):
    if d1 > d2:
        return 1
    elif d1 < d2:
        return -1
    else:
        return 0

def cmpDates(o1,o2):
    d1 = o1['datetime']
    d2 = o2['datetime']
    if d1 > d2:
        return False
    else:
        return True

# Funciones de ordenamiento
