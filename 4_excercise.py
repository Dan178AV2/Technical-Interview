from modulo import Ponquesito as pq
import matplotlib.pyplot as plt
import numpy as np

''' 
Utiliza la clase Ponquesito para hacer la transformacion de datos, puedes usar cualquier libreria para darle el formato
necesario a la data entregada para poder usar la clase.

IMPORTANTE: !No usar inteligencia artificial para la realizacion de este ejercicio! Aqui se mediran las brechas que requieren ser
tratadas en la hora de la capacitacion.
'''
data = ['-1F', '117F', '113C', '56C', '110C', '55F', '24C', '93C', '200C', '35F', '189C', '130C', '34F', '152F', '197F', '51F', '74C', '153F', '147F', '114C', '64C', '187F', '-2C', '158F', '86C', '130C', '164C', '81F', '16F', '52C', '140C', '181C', '55F', '-10C', '168F', '29C', '98F', '62F', '150F', '-6C', '11F', '88C', '138F', '57F', '39F', '97F', '51F', '43C', '150C', '179F', '55C', '13C', '129F', '102C', '4F', '10F', '12F', '159F', '12C', '192C', '155F', '78F', '164F', '162C', '139C', '123F', '160C', '62F', '39F', '62F', '97F', '71C', '91F', '125F', '88C', '177F', '0F', '74F', '156F', '-10F', '137F', '108C', '89F', '90C', '190C', '126F', '22C', '147C', '118C', '172F', '28F', '147C', '135C', '32C', '56F', '71F', '131C', '68F', '78F', '178F']



''' Aqui debe haber un listado con los valores transformados'''
resy = []

''' Genera una lista con los numeros del 1 al maximo tamaño de la lista resy'''
resx = [x for x in range(1,len(resy)+1)]

''' Codigo necesario para generar el mapa scatter'''
c = np.sqrt(resy)
fig, ax = plt.subplots(1,1, figsize=(7,7), dpi=120)
ax.scatter(resx,resy, marker='o', c=c)
plt.show()