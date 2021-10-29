#import numpy as np

Captura_Numero = []



def Validar_Numero(numero):
    #print('estos son los numeros ',numero)
    for i in numero:
        print(numero.isnumeric())
       # if i.isnumeric()==True:
     #       print('el numero del vector ')
    #    else:
    #        print('EL VECTOR TIENE UNA LETRA')


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
            #Captura_Numero.append(linea)
            #print('este son los numeros',linea)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")











Leer()
#input()



