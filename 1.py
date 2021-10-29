import numpy as np

Captura_Numero = []

def Crear():
    archivo = open("inicial.txt","w")
    archivo.close()

def Escribir():
    try:
        archivo = open("inicial.txt")
        print("escribe un texto")
        cadena = input()
        archivo.write(cadena+'\n')
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")



def Leer():
        try:
            archivo =open("inicial.txt","r")
            print("error al archivo",archivo)
            linea = archivo.readline()
            while(linea):
                print('ola mundo',linea)
                #Captura_Numero.append(linea)
                linea = archivo.readline()
            archivo.close()
        except FileNotFoundError:
            print ("NO EXISTE EL ARCHIVO")


#print('MATRIZ EN MAYUSCULA ',matriz[0][3])
# #a = [[1, 2, 3, 4], [5, 6,10,5], [7, 8, 9,4]]

#matrix = [] ; 

#matrix.append([1,2,3,4])

#print(matrix[0][3])





#Leer()
input()
