# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:10:46 2023

@author: Ricardo Ismael Gomez Sanchez
"""
grafo = {
'A':{'B':1, 'C':3, 'D':2, 'E':4},
'B':{'A':1, 'C':2},
'C':{'A':3, 'B':2, 'D':1},
'D':{'A':2, 'C':1, 'E':1},
'E':{'A':4, 'D':1}
}
#
def dijikstra (grafo, origen, destino):
    dis_más_corta = {}
    track_predecessor = {}
    unseenNodes = grafo
    infinito = 9999999
    pista =[]
     
    for nodo in unseenNodes:
        dis_más_corta[nodo] = infinito
    dis_más_corta[origen] = 0
    
    while unseenNodes: 
        dis_mín_nodo = None
        for nodo in unseenNodes:
            if dis_mín_nodo is None:
                dis_mín_nodo = nodo
            elif dis_más_corta[nodo] < dis_más_corta[dis_mín_nodo]:
                dis_mín_nodo = nodo
        Caminos = grafo[dis_mín_nodo].items()

        
        for nodo_nuevo, peso in Caminos:
            if peso + dis_más_corta[dis_mín_nodo] < dis_más_corta[nodo_nuevo]:
                dis_más_corta[nodo_nuevo] = peso + dis_más_corta[dis_mín_nodo]
                track_predecessor[nodo_nuevo] = dis_mín_nodo
        unseenNodes.pop(dis_mín_nodo) 
        print("Nodo actual:")
        print(dis_mín_nodo)
        print("Opciones de ruta:")
        print(Caminos)
        print("\n")
    Nodo_actual = destino

    while Nodo_actual != origen:         
        try:
            pista.insert(0, Nodo_actual)
            Nodo_actual =track_predecessor[Nodo_actual]
        except KeyError:
            print("Path is not reachable")
             
    pista.insert(0,origen)
    
    if dis_más_corta[destino] != infinito:
        print("La distancia más corta de '"+Ori+"' a '"+Des+"' es: " + str(dis_más_corta[destino]))
        print("Utilizando la ruta: " + str(pista))
#
Ori='B'
Des='E'    
dijikstra(grafo, Ori, Des)
