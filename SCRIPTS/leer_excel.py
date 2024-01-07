import openpyxl
import os

def excel ():
    #ruta del archivo "datos.xlsx" de excel
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_actual,'..', 'ARCHIVOS', 'datos.xlsx')
    excel = ruta_archivo
    
    #
    workbook = openpyxl.load_workbook(excel)

    nombre_de_la_hoja="s4"
    sheet = workbook.get_sheet_by_name(nombre_de_la_hoja)
    rango_celdas = sheet['B4:B13']
    valores = [celda[0].value for celda in rango_celdas]
    return valores

# Paleta de colores
def colores ():   
    color_palette = [
        (0.8, 0.2, 0.2, 1),  # Rojo
        (0.2, 0.8, 0.2, 1),  # Verde
        (0.2, 0.2, 0.8, 1),  # Azul
        (0.8, 0.8, 0.2, 1),  # Amarillo
        (0.2, 0.8, 0.8, 1),  # Cian
    ]
    