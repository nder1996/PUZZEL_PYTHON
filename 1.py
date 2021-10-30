#import numpy as np

Captura_Numero = []



def Validar_Numero(numero):
    captura = []
    for i in numero:
        if i.isdigit()==True:
            captura.append(i)
        else:
            continue
    Captura_Numero.append(captura)


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
        archivo = open("inicial.txt")
        linea = archivo.readline()
        while(linea):
            Validar_Numero(linea)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")











Leer()
#input()

print('ESTE ES LA MATRIX',Captura_Numero)


