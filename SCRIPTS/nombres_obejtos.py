import bpy
import openpyxl
import os

#2. Dependiendo de la altura que cambie de color


def excel ():
    
    excel_ruta = "/Users/andresguevara/Library/CloudStorage/OneDrive-UniversidadDistritalFranciscoJosédeCaldas/UNIVERSIDAD/pie 3d/PRUEBA FINAL/ARCHIVOS/datos.xlsx"
    workbook = openpyxl.load_workbook(excel_ruta)
    nombre_de_la_hoja="s4"
    sheet = workbook.get_sheet_by_name(nombre_de_la_hoja)
    rango_celdas = sheet['B4:B8']
    valores = [celda[0].value for celda in rango_celdas]
    valores_numericos = [float(valor) for valor in valores if valor is not None]
    
    return valores_numericos

valor_z=excel()

for i in range(1,6):
    
    asignacion=str(i).zfill(2)
    objeto_existente = bpy.data.objects.get(asignacion)
    objeto_existente.scale.z = valor_z[i-1] 

# # Paleta de colores
color_palette = [
    (0.8, 0.2, 0.2, 1),  # Rojo
    (0.2, 0.8, 0.2, 1),  # Verde
    (0.2, 0.2, 0.8, 1),  # Azul
    (0.8, 0.8, 0.2, 1),  # Amarillo
    (0.2, 0.8, 0.8, 1),  # Cian
]


        

    

