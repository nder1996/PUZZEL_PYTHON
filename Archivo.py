from collections import deque


captura_inicial = []

captura_final = []



def Validar_Numero(numero):
    completo = ''
    for i in numero:
        if i==',':
            captura_inicial.append(completo)
            completo=''
        else:
            completo +=i


def Validar_Numero_Final(numero):
    completo = ''
    for i in numero:
        if i==',':
            captura_final.append(completo)
            completo=''
        else:
            completo +=i


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
        #captura_inicial.pop();
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")

def Leer_1():
    try:    
        archivo = open("final.txt")
        linea = archivo.readline()
        while(linea):
            Validar_Numero_Final(linea)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")


if __name__ == "__main__":
    Leer()
    Leer_1()
 





