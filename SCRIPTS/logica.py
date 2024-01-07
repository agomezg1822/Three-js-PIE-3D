#import bpy
import pandas as pd
import numpy as np

nombre_objeto=0
for i in range(3):
    print(nombre_objeto+i)


nombre_objeto_01 = "01"
nombre_objeto_02 = "02"
nombre_objeto_03 = "03"

nuevo_valor_z_objeto_01 = 1
nuevo_valor_z_objeto_02 = 1
nuevo_valor_z_objeto_03 = 1
valor_origen=1

objeto_01 = bpy.data.objects.get(nombre_objeto_01)
objeto_01.scale.z = nuevo_valor_z_objeto_01

objeto_02 = bpy.data.objects.get(nombre_objeto_02)
objeto_02.scale.z = nuevo_valor_z_objeto_02

objeto_03 = bpy.data.objects.get(nombre_objeto_03)
objeto_03.scale.z = nuevo_valor_z_objeto_03





