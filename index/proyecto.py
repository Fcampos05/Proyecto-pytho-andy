import math
import xlsxwriter

# Crea una matriz con valores específicos
matriz = [["TRAMO   ","f   ", "L   ", "D   ","Q","     r","           rQ^2","              signo(rQ^2)","              |2rQ|","              Qr"], 
         ["AB",0.02, 800, 0.75,1,5,6,7,8,0], 
         ["BC",0.02, 850, 0.75,1,5,6,7,8,0], 
         ["CD",0.02, 850, 0.75,0.3,5,6,7,8,0],
         ["AD",0.02, 700, 0.75,-0.5,5,6,7,8,0],
         [0,0, 0, 0,0,0,0,0,0,0],
         [0,0, 0, 0,0,0,0,0,0,0]]

matriz2 = [["TRAMO   ","f   ", "L   ", "D   ","Q","     r","           rQ^2","              signo(rQ^2)","              |2rQ|","              Qr"],
         ["AD",0.02, 700, 0.75,0.5,5,6,7,8,0], 
         ["DF",0.02, 650, 0.75,-0.2,5,6,7,8,0], 
         ["EF",0.02, 750, 0.75,-0.5,5,6,7,8,0],
         ["AE",0.02, 1200, 0.75,-1.5,5,6,7,8,0],
         [0, 0, 0,0,0,0,0,0,0],
         [0, 0, 0,0,0,0,0,0,0]]

matriz3 = [["TRAMO   ","f   ", "L   ", "D   ","Q","     r","           rQ^2","              signo(rQ^2)","              |2rQ|","              Qr"],
         ["CD",0.02, 850, 0.75,-0.3,5,6,7,8,0], 
         ["CG",0.02, 750, 0.75,0.7,5,6,7,8,0], 
         ["FG",0.02, 800, 0.75,-0.3,5,6,7,8,0],
         ["DF",0.02, 650, 0.75,0.2,5,6,7,8,0],
         [0, 0, 0,0,0,0,0,0,0],
         [0, 0, 0,0,0,0,0,0,0]]

def add_to_matrix(matrix):
  matrix[5][6]=0
  matrix[5][7]=0
  for i, row in enumerate(matrix):

        if i<=4 and i>=1:
                matrix[i][5]=(8*matrix[i][1]*matrix[i][2])/(pow(math.pi, 2)*9.81*pow(matrix[i][3], 5))
                matrix[i][6]=matrix[i][5]*pow(matrix[i][4], 2)
                matrix[i][7]=(matrix[i][4]/abs(matrix[i][4]))*matrix[i][6]
                matrix[i][8]=abs(2*matrix[i][4]*matrix[i][5])
                matrix[5][6]=matrix[5][6]+matrix[i][7]        
                matrix[5][7]=matrix[5][7]+matrix[i][8]

  matrix[6][5]=-matrix[5][6]/matrix[5][7]


def search_and_qf(matrix,matrix2,matrix3):
  for i, row in enumerate(matrix):
        if i<=4 and i>=1:
            a1=search_and_valor(matrix2, matrix[i][0])
            a2=search_and_valor(matrix3, matrix[i][0])
            matrix[i][9]=matrix[i][4]+matrix[6][5]-a1-a2
  for i, row in enumerate(matrix2):
        if i<=4 and i>=1:
            a1=search_and_valor(matrix, matrix2[i][0])
            a2=search_and_valor(matrix3, matrix2[i][0])
            matrix2[i][9]=matrix2[i][4]+matrix2[6][5]-a1-a2
  for i, row in enumerate(matrix3):
        if i<=4 and i>=1:
            a1=search_and_valor(matrix2, matrix3[i][0])
            a2=search_and_valor(matrix, matrix3[i][0])
            matrix3[i][9]=matrix3[i][4]+matrix3[6][5]-a1-a2


def replace_and_qf(matrix,matrix2,matrix3):
  for i, row in enumerate(matrix):
        if i<=4 and i>=1:
            matrix[i][4]=matrix[i][9]
            matrix[i][9]=0
  for i, row in enumerate(matrix2):
        if i<=4 and i>=1:
            matrix2[i][4]=matrix2[i][9]
            matrix2[i][9]=0
  for i, row in enumerate(matrix3):
        if i<=4 and i>=1:
            matrix3[i][4]=matrix3[i][9]
            matrix3[i][9]=0




def search_and_valor(arr, element):
    for sub_arr in arr:
        if element in sub_arr:
            return arr[6][5]
    return 0        


def agregar_arreglo(array_of_arrays, arr):
    array_of_arrays.append(arr)
    return array_of_arrays


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



def print_matrix(matrix):
  for row in matrix:
    for element in row:
      print(element, end='      ')
    print("")
  print("--------------------------------------------------------------------------")  

array_of_arrays = []


add_to_matrix(matriz)
add_to_matrix(matriz2)
add_to_matrix(matriz3)

search_and_qf(matriz,matriz2,matriz3)

print_matrix(matriz)
print_matrix(matriz2)
print_matrix(matriz3)

arreglo=[]

arreglo=matriz+matriz2+matriz3


exportar_arreglos_bidimensionales('iteracion01.xlsx', arreglo)

i=2
arreglo2=[]
while (abs(matriz[6][5])+abs(matriz2[6][5])+abs(matriz3[6][5]))/3 > 0.0000001:
  
  print("----------------------------------------------------------------------------------------------------------------------------")  
  print("ITERACION "+ str(i))
  replace_and_qf(matriz,matriz2,matriz3)

  add_to_matrix(matriz)
  add_to_matrix(matriz2)
  add_to_matrix(matriz3)

  search_and_qf(matriz,matriz2,matriz3)
  arreglo2=matriz+matriz2+matriz3
  if i<=9:
    exportar_arreglos_bidimensionales('iteracion0'+str(i)+'.xlsx', arreglo2)
  if i>9:
    exportar_arreglos_bidimensionales('iteracion'+str(i)+'.xlsx', arreglo2)
  
  i+=1
  print("##############################################################################################################################################################----")  
  print_matrix(arreglo2)
  print("##############################################################################################################################################################----")
  
  


