

import pprint
import math
pp = pprint.PrettyPrinter(indent=4)
from array import array
dim=rows=cols=4

from Archivo import *


class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.middle1 = None
        self.right = None
        self.middle2=None
		
		
class Tree:
    def crearNodo(self, data):
        return Node(data)

    def insertarNodo(self, node , data):
        if node is None:
            return self.crearNodo(data)
        if node.data==data:
            return node
        elif node.left==None:
            node.left = self.insertarNodo(node.left, data)
        elif node.right==None:
            node.right = self.insertarNodo(node.right, data)
        elif node.middle1==None:
            node.middle1 = self.insertarNodo(node.middle1, data)	
        else:
            node.middle2 = self.insertarNodo(node.middle2, data)

        return node
		
    def search(self, node, data):
        if node.data == data:
            return node
        if node.right!=None:
            return self.search(node.right, data)
        elif node.left!=None:
            return self.search(node.left, data)
        elif node.middle1!=None:
            return self.search(node.middle1, data)			
        elif node.middle2!=None:
            return self.search(node.middle2, data)

    def traversePreorder(self, root,pos=5):
        if root is not None:
            space=" "
            q=root.data
            print(space,q)
            self.traversePreorder(root.left,pos-2)
            self.traversePreorder(root.right,pos-1)
            self.traversePreorder(root.middle1,pos)
            self.traversePreorder(root.middle2,pos+1)        

tree=Tree()
def linearverticalconflict(mat):
	puzz=eval(mat)
	lc=0
	for fila in range(4):
		max=-1
		for col in range(4):
			valorCelda=puzz[fila][col]
			if valorCelda !=0 and (valorCelda-1)/dim == fila:
				if valorCelda>max:
					max=valorCelda
				else:
					lc +=2
	return lc					
	
def linearhorizontalconflict(mat):
	puzz=eval(mat)
	lc=0
	for col in range(4):
		max=-1
		for fila in range(4):
			valorCelda=puzz[fila][col]
			if valorCelda !=0 and valorCelda%dim == col+1:
				if valorCelda>max:
					max=valorCelda
				else:   
					lc +=2
	
	return lc

def linearconflict(puzz):
	h=distancia(puzz)
	h += linearverticalconflict(puzz)
	h += linearhorizontalconflict(puzz)
	return h  
  
def esResolvible(mat):
    puzzle=eval(mat)
    igualdad=0
    gridwidth=len(puzzle)
    puzz=[]
	
    for x in puzzle:
        for elt in x:
            puzz.append(elt)			
    # print ('ancho de cuadricula') 
    fila=0
    celdaFIla=0
    for i in range(0,len(puzz)):
        j=i+1
        if i % gridwidth == 0:
            fila+=1
        if puzz[i]==0:
            celdaFIla=fila
            print ('celda %d'% celdaFIla)
            continue 
        for j in range(i+1,len(puzz)):
             if puzz[i]>puzz[j] and puzz[j]!=0:
                 igualdad+=1
        print ('igualdad %d'% igualdad)

    if gridwidth % 2 == 0: 
        if celdaFIla % 2 == 0: 
            return igualdad % 2 != 0;
        else: 
            return igualdad % 2 == 0;
        
    else: 
        return igualdad % 2 == 0;
		
def A_star(puzz,goal,root):
   
    frente = [[distancia(puzz), puzz]] 
    expanded = []
    expanded_states=0
    while frente:
        i = 0
        for j in range(1, len(frente)):
            if frente[i][0] > frente[j][0]:
                i = j
        path = frente[i]
        frente = frente[:i] + frente[i+1:]
        finNodo = path[-1]
        if finNodo == goal:
            break
        if finNodo in expanded: continue
        for k in movimientos(finNodo,root):
            if k in expanded: continue
            newpath = [path[0] + distancia(k) - distancia(finNodo)] + path[1:] + [k] 
            frente.append(newpath)
            expanded.append(finNodo)
        expanded_states += 1 
    print ("Nodos expandidos:", 
	expanded_states)
    print ("Solucion:")
    pp.pprint(path)


def movimientos(mat,root): 
   
    output = []  

    m = eval(mat)  
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); 

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    tree.insertarNodo(root,output)
    return output


def distancia(mat):
     
    distancia = 0
    puzz = eval(mat) 
    
    for i in range(rows):
        for j in range(cols):
	
            puzz[i][j]=int(puzz[i][j])
            if puzz[i][j] == 0 : continue
            distancia += abs(i - puzz[i][j] / 4)
            distancia +=abs(j -  (puzz[i][j]%4))
    return distancia

	

	
if __name__ == '__main__':
    Leer()
    Leer_1()
    numbers = captura_inicial.copy()
    puzzle = str([numbers[i:i+rows] for i in range(0, len(numbers), rows)])
    goal = captura_final.copy()
    
    #str([[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]])    
    root=tree.root=None
    if esResolvible(puzzle) : 
        print ("resolvible")	
        root=tree.insertarNodo(root, puzzle)
        tree.traversePreorder(root)
        print(char(x) for x in input())
        A_star(puzzle,goal,root)
    else:
        print("no resolvible") 
    


        
        