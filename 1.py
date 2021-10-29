#import numpy as np

#Captura_Numero = []

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
        archivo = open("inicial12.txt")
        linea = archivo.readline()
        while(linea):
            print(linea)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")
  






Leer()
input()


