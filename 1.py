

def Crear():
    archivo = open("Busqueda.txt","w")
    archivo.close()

def Escribir():
    archivo = open("Busqueda.txt","a")
    print("escribe un texto")
    cadena = input()
    archivo.write(cadena+'\n')
    archivo.close()

def Leer():
    archivo = open("Busqueda.txt","r")
    linea = archivo.readline()
    while(linea):
        print(linea)
        linea = archivo.readline()
    archivo.close()

