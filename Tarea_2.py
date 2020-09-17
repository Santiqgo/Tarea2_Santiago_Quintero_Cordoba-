#!/usr/bin/env python
# coding: utf-8

import Vector #Se importa como modulo a las clases creadas en "Vector.py"
from math import acos,atan,sin,cos,pi#Cuando se hizo la prueba en un mismo notebook hay errores debido a la falta de importar estas librerías cosa que no pasa cuando se usa import Vector, para que no aparezca dicho fallo se importan pero no se espera que sea necesario

########Vectores pedidos############################
a=Vector.VectorCartesiano(1.5,0,2.4)
b=Vector.VectorCartesiano(0,1,9)
c=Vector.VectorCartesiano(4.2,0.05,0)
####################################################################

#A los vectores entregados se les va a calcular las componentes polares(no se calcula el vector polar,siguen estando en la base i,j,k) y luego se mostraran
print((Vector.VectorCartesiano.cartesianoapolar(a)).cartesiano)
print((Vector.VectorCartesiano.cartesianoapolar(b)).cartesiano)
print((Vector.VectorCartesiano.cartesianoapolar(c)).cartesiano)
########################################################################

######Como los vectores son reales pertenecientes a R3 se calcula el producto interno entre todos sabiendo que en dicho espacio el producto interno es conmutativo
print((a*b).cartesiano)
print((a*c).cartesiano)
print((b*c).cartesiano)
########################################################################

#######Se calculan 3 de los 6 productos cruces entre los elementos (sabiendo que axb=-bxa y axa=0) dados
print(Vector.VectorCartesiano.Cruz(a,b).cartesiano)
print(Vector.VectorCartesiano.Cruz(a,c).cartesiano)
print(Vector.VectorCartesiano.Cruz(b,c).cartesiano)
#############################################

############################por ultimo se llama el modulo para calcular el angulo entre dos vectores
print(Vector.VectorCartesiano.angulo(a,b))
print(Vector.VectorCartesiano.angulo(a,c))
print(Vector.VectorCartesiano.angulo(b,c))
###################################################