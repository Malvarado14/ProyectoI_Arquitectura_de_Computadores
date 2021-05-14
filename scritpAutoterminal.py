import shutil, os
import sys
import subprocess
from subprocess import Popen, PIPE, call
import numpy as np
from numpy import *

direct = "/home/estudiante/"
wd = "export BENCHMARK=$HOME/benchmark/"
runGem5 = "/home/estudiante/run_gem5_part2.sh"

matriz = np.zeros((0,4)) # Matriz vacía
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                matriz = append(matriz,[pow(2,a),pow(2,b),pow(2,c),pow(2,(3+d))]) # Array vacía que contiene todas las combinaciones de data

parametros = reshape(matriz,(81,4)) # Matriz vacía que contiene todas las combinaciones de data
indice = [201,215,228,247] # assocDataL1, assocInstL1, assocL2, cacheline_size


def direcciones(ruta):
    return [ruta+"adpcm/", ruta+"aes/", ruta+"blowfish/",ruta+"dfmul/",ruta+"dfsin/",ruta+"fft/",ruta+"fir/",ruta+"gsm/",ruta+"jpeg/",ruta+"matrixmultiply/",ruta+"motion/",ruta+"sha/"]
#return [ruta+"adpcm/", ruta+"aes/", ruta+"blowfish/",ruta+"dfmul/",ruta+"dfsin/",ruta+"fft/",ruta+"fir/",ruta+"gsm/",ruta+"jpeg/",ruta+"matrixmultiply/",ruta+"motion/",ruta+"sha/"]

myfile = open(runGem5,"r")
lines = myfile.readlines() # Contiene la información de la lectura de toda una línea del archivo
    
original = lines[3].replace(lines[3][247:],'8') # PATCH al bug raro que adjunta números al final de la línea -> 8 -> 16 ->? 8 -> 86
#print("\n\nORIGINAL="+str(original)+"\n\n")


suma = ""
for x in range(len(direcciones("/home/estudiante/benchmark/"))): # Aquí se supone que cambia de directorio 12 veces para cada archivo de compilación ######## range(len(direccion)) #########
    for y in range(len(parametros)): # N significa la cantidad de pruebas a realizar ###### range(len(parametros)) #########
        for z in range(4):
            if(z==0):
                suma = original[:(indice[z])]+str(int(parametros[y][z]))+original[(indice[z]+1):] # Falta agregar primer parentesis de matriz para  parámetros
                #print("suma en ["+str(z)+"]: \n"+str(suma)+"\n")
            else:
                suma = suma[:(indice[z])]+str(int(parametros[y][z]))+suma[(indice[z]+1):]
                #print("suma en ["+str(z)+"]: \n"+str(suma)+"\n")

        ruta = direcciones(wd)[x]+"gcc" ####### Parámetro a cambiar de gcc por clang (o en general el nombre del archivo compilado) ###########
        lines[1] = ruta
    
        sumaF = "\n"+suma
        lines[3] = sumaF

        myfile = open(runGem5,"w")
        myfile.writelines(lines)
        myfile.close()    

        inst = subprocess.run(["./run_gem5_part2.sh"],stdout=PIPE,shell=True,cwd=direct) # Acceso a terminal para compilar runGem5
        print(inst.stdout)    

        os.rename(r'/home/estudiante/m5out/stats.txt',r'/home/estudiante/'+str(direcciones("benchmark/")[x])+'stats_'+str(y)+'.txt') # Trasladar archivo & cambia name
