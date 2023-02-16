import xlsxwriter

def export_to_excel(array_of_arrays, file_name):
    # Crea una nueva hoja de trabajo
    workbook = xlsxwriter.Workbook(file_name)
    
    for array in array_of_arrays:
        # Crea una nueva hoja en el libro de trabajo
        worksheet = workbook.add_worksheet()
        
        # Recorre cada fila en el arreglo bidimensional
        for row_index, row in enumerate(array):
            # Recorre cada elemento en la fila
            for col_index, value in enumerate(row):
                # Escribe el valor en la celda correspondiente
                worksheet.write(row_index, col_index, value)
    
    # Cierra el libro de trabajo
    workbook.close()
# Crea una lista de arreglos bidimensionales

def join_arrays(array_of_arrays):
    result = []
    for arr in array_of_arrays:
        result.extend(arr)
    return result

array1 = [[1, 2, 3], [4, 5, 6]]
array2 = [[7, 8, 9], [10, 11, 12]]

array_of_arrays = [array1,array2]

a=[]
a=join_arrays(array_of_arrays)
# Llama a la función para exportar los arreglos a un archivo Excel
export_to_excel(a, 'array_of_arrays323.xlsx')


# Ejemplo de uso
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 2, 6768], [4, 5, 6], [7, 8, 9]]
filename = "arreglo2.xlsx"
print("")
