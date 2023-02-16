import xlsxwriter

def export_arrays_to_excel(file_name, sheet_name, arrays):
    """
    Función que exporta varios arreglos bidimensionales a una hoja de excel.
    :param file_name: nombre del archivo excel
    :param sheet_name: nombre de la hoja de excel
    :param arrays: lista de arreglos bidimensionales a exportar
    :return: None
    """
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet(sheet_name)
    
    row = 0
    for array in arrays:
        col = 0
        for item in array:
            worksheet.write(row, col, str(item))
            col += 1
        row += 1

    workbook.close()

array1 = [[1, 2, 3], [4, 5, 6]]
array2 = [[7, 8, 9], [10, 11, 12]]
array3 = [[7, 8, 9], [10, 11, 12]]

export_arrays_to_excel("array_data.xlsx", "Sheet 1", [array1, array2, array3])
