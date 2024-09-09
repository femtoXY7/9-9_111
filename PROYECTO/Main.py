'''
import Funciones #trae todo el modulo, para acced
Funciones.saludar("Hola 111") # para invocar la funcion con el import haya q poner "nombredelmodulo.funcion"
se esta como copiando y pegando todo, en un sistema compilado es nefasto

'''
'''para traer solo una parte del modulo
from Paquete.Funciones import saludar,saludar_profesor #desde modulo traer la funcion, solo importas lo que te interesa 
saludar_profesor("Pepe","Tecnologia")
from Paquete.Funciones import * #para importar todo como import modulo, pero te evitas poner "modulo.funcion"
'''

'''
PAQUETERIA:
from Paquete.Funciones import * #desde paquete.modulo
#se pueden agrupar en paquetes
saludar("HOLA GENTE")
'''
'''
from .Paquete.Otro_modulo import prueba #para hacer referencia a un modulo que esta dentro del mismo paquete
'''

from .Paquete.Otro_modulo import prueba
