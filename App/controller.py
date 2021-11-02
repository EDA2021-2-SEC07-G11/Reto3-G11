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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    return model.newCatalog()

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFOfile = cf.data_dir + 'UFOS/UFOS-utf8-large.csv'
    input_file = csv.DictReader(open(UFOfile, encoding='utf-8'))
    for avistamiento in input_file:
        model.agregarAvistamiento(catalog, avistamiento)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def darAvistamientosCiudad(catalog, ciudad):
    return model.darAvistamientosCiudad(catalog, ciudad)

def darInfoReq1(lista):
    return model.infoReq1(lista)

def darInfoReq2(lista):
    return model.infoReq2(lista)

def darInfoReq6(lista):
    return model.infoReq6(lista)

def darMapaRangoDuracion(catalog, inf, sup):
    return model.darAvistamientosDuraciones(catalog, inf, sup)

def darMapaRangoFechas(catalog, inf, sup):
    return model.darAvistamientosFechas(catalog, inf, sup)

def darListaDuraciones(raiz, lista):
    return model.listaDuraciones(raiz, lista)

def darListaFechas(raiz, lista):
    return model.listaFechas(raiz, lista)

def darMapaCoordenadas(catalog, longInf, longSup, latInf, latSup):
    return model.darAvistamientosZona(catalog, longInf, longSup, latInf, latSup)

def darListaZonas(raiz, lista):
    return model.listaZonas(raiz, lista)

