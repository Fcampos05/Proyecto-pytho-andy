import xlsxwriter

def exportar_arreglos_bidimensionales(nombre_archivo, *arreglos):
    # Crea un archivo de Excel
    workbook = xlsxwriter.Workbook(nombre_archivo)

    # Agrega una hoja de cálculo al archivo de Excel
    worksheet = workbook.add_worksheet()

    fila_inicial = 0
    columna_inicial = 0

    # Escribir los datos de cada arreglo bidimensional en la hoja de cálculo
    for arreglo in arreglos:
        for i, row in enumerate(arreglo):
            for j, value in enumerate(row):
                worksheet.write(fila_inicial + i, columna_inicial + j, value)
        fila_inicial += len(arreglo)

    # Cierra el archivo de Excel
    workbook.close()

# Ejemplo de uso
arreglo1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arreglo2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

exportar_arreglos_bidimensionales("arreglos_bidimensionales.xlsx", arreglo1, arreglo2)
