# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:06:33 2020

@author: DiegoAll
"""
import numpy as m

#Funcion que lee los puntos
def leerVtk(archivo):
    entrada=open(archivo,'r')
    linea=entrada.readline()   
    cont=0
    while linea.find("POINTS") == -1:
        linea=entrada.readline()
    lineaPuntos=linea.split(' ')
    nroPuntos=lineaPuntos[1]
    cont=0
    listaPuntos = []
    while cont < int(nroPuntos):
        cont=cont+1
        linea= [float(i) for i in entrada.readline().strip().split(' ')]
        listaPuntos.append(linea) 
    linea=entrada.readline()  
    #para que encuentre donde aparezca cells 
    while linea.find("CELLS")== -1:
        linea=entrada.readline()
    #la primera ocurrencia de un triangulo
    while linea[0]!='3': 
        linea=entrada.readline()
    linea = [int(i) for i in linea.strip().split(' ')]
    listaTriangulos= [linea[1:4]]
    #print(listaTriangulos) #Debugging
    while linea[0]==3:
        try:
            linea=[int(i) for i in entrada.readline().strip().split(' ')]
            listaTriangulos.append(linea[1:4])
        except:
            linea=[0]
    #print (listaTriangulos) #Debugging
    return listaPuntos,listaTriangulos

puntos,triangulos=leerVtk('circulo.vtk')

def calcularAltura(x,y):
    f = lambda x,y: m.sqrt(1 - x**2 - y**2 + 0.j)
    t=(f(x,y))
    return t   
valor=calcularAltura(0,1)
print(valor)

print (len(triangulos))
volumenTotal=0
for   i  in range(len(triangulos)):
    a=m.sqrt((puntos[triangulos[i][0]][0]-puntos[triangulos[i][1]][0])**2+(puntos[triangulos[i][0]][1]-puntos[triangulos[i][1]][1])**2)
    b=m.sqrt((puntos[triangulos[i][1]][0]-puntos[triangulos[i][2]][0])**2+(puntos[triangulos[i][1]][1]-puntos[triangulos[i][2]][1])**2)
    c=m.sqrt((puntos[triangulos[i][0]][0]-puntos[triangulos[i][2]][0])**2+(puntos[triangulos[i][0]][1]-puntos[triangulos[i][2]][1])**2)
    s=(a+b+c)/2.0
    areaTriangulo=m.sqrt(s*(s-a)*(s-b)*(s-c)) 
    print (triangulos[i][0],triangulos[i][1],triangulos[i][2],"El area es: ", areaTriangulo)  
    
    h0=calcularAltura(puntos[triangulos[i][0]][0],puntos[triangulos[i][0]][1])
    h1=calcularAltura(puntos[triangulos[i][1]][0],puntos[triangulos[i][1]][1])
    h2=calcularAltura(puntos[triangulos[i][2]][0],puntos[triangulos[i][2]][1])
    altura=(h0+h1+h2)/3.0
    volumen=areaTriangulo*altura
    volumenTotal=volumenTotal+volumen


print("El volumen total es: ", volumenTotal)
    
    
            



#print("LISTA DE PUNTOS")
#print(puntos)
#print()
#print("LISTA DE TRIANGULOS")
#print(triangulos)

