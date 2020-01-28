"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lst.append(row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos Archivos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst1, lst2, lst3, lst4):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """

    if len(lst1)==0 or len(lst2)==0:
        print("Alguna lista esta vacía")  
        return 0
    else:
        #en primer lugar busco las películas que cumplen la condicion en los archivos de menor tamaño

        t1_start = process_time() #tiempo inicial

        listaIds = [] #se instancia lista para los Ids de las películas del director

        for element in lst1:   #se crea una lista con los Ids de las películas del director
            if criteria.lower() in element[column].lower():
                listaIds.append(element["id"])

        counterSmall=0
        for a in listaIds:  #se busca en la lista con detalles de las películas aquellas con el id guardado que tengan puntaje igual o mayor a 6
            for b in lst2:
                
                if int(a) == int(b["id"]) and float(b["vote_average"]) >= 6: 
                    counterSmall=counterSmall+1

        
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución archivos pequenos",t1_stop-t1_start," segundos")

        #ahora busco las películas que cumplen la condicion en los archivos de mayor tamaño para comparar 

        t2_start = process_time() #tiempo inicial

        listaIdsAll = [] #se instancia lista para los Ids de las películas del director

        for element in lst3:   #se crea una lista con los Ids de las películas del director
            if criteria.lower() in element[column].lower():
                listaIdsAll.append(element["id"])

        counterAll=0
        for a in listaIdsAll:  #se busca en la lista con detalles de las películas aquellas con el id guardado que tengan puntaje igual o mayor a 6
            for b in lst4:
                
                if int(a) == int(b["id"]) and float(b["vote_average"]) >= 6: 
                    counterAll=counterAll+1

        
        t2_stop = process_time() #tiempo final
        print("Tiempo de ejecución archivos grandes",t2_stop-t2_start," segundos")

        
        answer =  "El criterio seleccionado fue: "+criteria+"\nCoinciden "+str(counterSmall)+" películas con vote_average igual o mayor a 6 con los archivos pequeños. \nCoinciden "+str(counterAll)+" peliculas con vote_average igual o mayor a 6 con los archivos grandes."
        return answer

    """
    La solución propuesta tendría una complejidad de orden O(n²) 
    """

def main():
    listaCast_small = [] #instanciar una lista vacia
    listaDetails_small = []
    listaCast_all = []
    listaDetails_all = []

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/MoviesCastingRaw-small.csv", listaCast_small) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(listaCast_small))+" elementos cargados")
                loadCSVFile("Data/SmallMoviesDetailsCleaned.csv",listaDetails_small) #llamar funcioń cargar datos del otro archivo
                print("Datos cargados, "+str(len(listaDetails_small))+" elementos cargados")
                loadCSVFile("Data/AllMoviesCastingRaw.csv", listaCast_all) #archivo grande
                print("Datos cargados, "+str(len(listaCast_all))+" elementos cargados")
                loadCSVFile("Data/AllMoviesDetailsCleaned.csv",listaDetails_all) #archivo grande
                print("Datos cargados, "+str(len(listaDetails_all))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(listaCast_small))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria, "actor1_name", listaCast_small) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                answer=countElementsByCriteria(criteria,"director_name",listaCast_small,listaDetails_small,listaCast_all,listaDetails_all)
                print(answer)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
