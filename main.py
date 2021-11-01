from collections import deque


from Archivo import *

inicial = []
final  = []


''''''
Leer()
Leer_1()


for i in  range(len(captura_inicial)):
    inicial.append(int(captura_inicial[i]))

for i in  range(len(captura_final)):
    final.append(int(captura_final[i]))
''''''




class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):        
        self.estado = estado                        
        self.padre = padre                          
        self.movimiento = movimiento               
        self.profundidad = profundidad             
        self.piezas_correctas = piezas_correctas   

  
    def mover(self, direccion):
        estado = list(self.estado)
        ind = estado.index(0)

        if direccion == "arriba":            
            if ind not in [12, 13, 14,15]:                
                temp = estado[ind + 3]
                estado[ind + 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "abajo":            
            if ind not in [0, 1, 2,3]:                
                temp = estado[ind - 3]
                estado[ind - 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "derecha":            
            if ind not in [0, 3, 6,9]:                
                temp = estado[ind - 1]
                estado[ind - 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "izquierda":            
            if ind not in [3, 7, 11,15]:                
                temp = estado[ind + 1]
                estado[ind + 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None        

 
    def encontrar_sucesores(self):
        sucesores = []
        sucesorN = self.mover("arriba")
        sucesorS = self.mover("abajo")
        sucesorE = self.mover("derecha")
        sucesorO = self.mover("izquierda")
        
        sucesores.append(Nodo(sucesorN, self, "arriba", self.profundidad + 1, calcular_heurisitica(sucesorN)))
        sucesores.append(Nodo(sucesorS, self, "abajo", self.profundidad + 1, calcular_heurisitica(sucesorS)))
        sucesores.append(Nodo(sucesorE, self, "derecha", self.profundidad + 1, calcular_heurisitica(sucesorE)))
        sucesores.append(Nodo(sucesorO, self, "izquierda", self.profundidad + 1, calcular_heurisitica(sucesorO)))
        
        sucesores = [nodo for nodo in sucesores if nodo.estado != None]  
        return sucesores


    def encontrar_camino(self, inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

 
    def imprimir_nodo(self):
        renglon = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" - ", end = " - ")
            else:
                print (pieza, end = " - ")
            renglon += 1
            if renglon == 4:
                print()
                renglon = 0       


def calcular_heurisitica(estado):
    correcto = (1, 2, 3, 4, 5, 6, 7, 8, 9 ,10,11,12,13,14,15,0)
    valor_correcto = 0
    piezas_correctas = 0
    if estado:
        for valor_pieza, valor_correcto in zip(estado, correcto):
            if valor_pieza == valor_correcto:
                piezas_correctas += 1
            valor_correcto += 1
    return piezas_correctas   


def bfs(inicial, meta):
    visitados = set()
    frontera = deque() 
    frontera.append(Nodo(inicial, None, None, 0, calcular_heurisitica(inicial)))
    
    while frontera:                         
        nodo = frontera.popleft()        
        if nodo.estado not in visitados:   
            visitados.add(nodo.estado)     
        else:                           
            continue                  
        
        if nodo.estado == meta:                    
            print("\n¡Se encontró la meta!")            
            return nodo.encontrar_camino(inicial)             
        else:                                           
            frontera.extend(nodo.encontrar_sucesores()) 


def dfs(inicial, meta, profundidad_max):
    visitados = set() 
    frontera = deque()  
    frontera.append(Nodo(inicial, None, None, 0, calcular_heurisitica(inicial)))
    
    while frontera:                      
        nodo = frontera.pop()              

        if nodo.estado not in visitados:   
            visitados.add(nodo.estado)     
        else:                           
            continue                    
        
        if nodo.estado == meta:            
            print("\n¡Se encontró la meta!")            
            return nodo.encontrar_camino(inicial)
        else:                                      
            if profundidad_max > 0:                           
                if nodo.profundidad < profundidad_max:                       
                    frontera.extend(nodo.encontrar_sucesores()) 
            else:                                              
                frontera.extend(nodo.encontrar_sucesores())     


def hc(inicial):
    visitados = set() 
    nodo_actual = Nodo(inicial, None, None, 0, calcular_heurisitica(inicial))

    while nodo_actual.piezas_correctas <16:            
        sucesores = nodo_actual.encontrar_sucesores()   
        max_piezas_correctas = -1


        for nodo in sucesores:   
            if nodo.piezas_correctas >= max_piezas_correctas and nodo not in visitados:
                max_piezas_correctas = nodo.piezas_correctas
                nodo_siguiente = nodo
            visitados.add(nodo_actual)

        if nodo_siguiente.piezas_correctas >= nodo_actual.piezas_correctas:
            nodo_actual = nodo_siguiente
     
        else:
            print("\nSe llegó a un máximo local. No se encontró la meta.")
            break
    else:
        print("\n¡Se encontró la meta!")        
    return nodo_actual.encontrar_camino(inicial)


def main():

    estado_final = tuple(final)
    estado_inicial = tuple(inicial)
    print("El estado inicial del juego es: ")
    (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
    print("\n¿Qué algoritmo desea correr? Escriba:")
    print("\t\"1\" para  correr Busqueda primero en anchura")
    algoritmo = input("Su elección: ")

  
    if algoritmo == "1" or algoritmo == "BFS":
        print("Corriendo BFS. Por favor espere.")
        nodos_camino = bfs(estado_inicial, estado_final)    
    else:
        return 0

    if nodos_camino:
        print ("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = (input ("¿Desea imprimir dicho camino? s/n: "))

        if imprimir_camino == "s" or imprimir_camino == "S":
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
            print ("Piezas correctas:", calcular_heurisitica(estado_inicial), "\n")
            input("Presione \"enter\" para continuar.")
            
            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                print("Piezas correctas:", nodo.piezas_correctas, "\n")     
                input("Presione \"enter\" para continuar.")
    else:
        print ("\nNo se encontró un camino con las condiciones dadas.")

    return 0    


if __name__ == "__main__":
    main()