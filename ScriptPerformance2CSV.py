import os, fnmatch, csv

print("pwd: "+os.getcwd()+"\n") #tst
cwd = os.getcwd()

temp = fnmatch.filter(os.listdir(cwd), "*.txt") # Lee y filtra todos los archivos de extensión '.txt' en la ruta donde está el archivo de Python.
files = sorted(temp) # Los ordena en orden alfabético
print(files) #tst

array1 = [6] # Líneas estratégicas en donde está la información relevante
nombres = ["Archivo","HostSeconds" ] 
salida = [x[:] for x in [[None] * (len(array1)+2)] * len(files)] # Forma eficiente de generar una matriz vacía

contadorj = 0
for j in files:
    myfile = open(j, "rt")
    #print(j) #tst
    line = myfile.readlines() # Contiene la información de la lectura de toda 1 línea del archivo
    
    contadori = 0
    salida[contadorj][contadori] = j # Coloca el nombre del archivo que se está leyendo en la primera posición
    for i in array1:
        dato = line[i].split() # Extrae de la línea leída, el segundo dato (cuando se separa por espacios en blanco de la línea entera)
        salida[contadorj][contadori+1] = dato[1] # Coloca consecuentemente cada dato, que corresponde al que hay en 'array1'
        contadori += 1

    #salida[contadorj][len(array1)+1] = float(salida[contadorj][3])/float(salida[contadorj][2])  # Le agrega el CPI al final
    contadorj += 1
    myfile.close()

nombreDelArchivo = 'performance.csv'

with open(nombreDelArchivo, 'w+', newline = '') as file:
    writer = csv.writer(file, delimiter = ';', quoting=csv.QUOTE_ALL)
    writer.writerow(nombres) # Escribe los identificadores (array 1D) en una fila [por eso el writer.writerow]
    writer.writerows(salida) # Escribe los datos de cada archivo (matrix 2D) en un conjunto de filas [por eso el writer.writerows]
print("\nArchivo compilador de diagnósticos generado con éxito. Revise en la carpeta por \""+nombreDelArchivo+"\"")
