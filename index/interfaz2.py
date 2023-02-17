import tkinter as tk
import math
import xlsxwriter
# Crear la ventana principal
root = tk.Tk()
ancho_ventana = 1100
altura_ventana = 180

# Obtenemos las dimensiones de la pantalla
ancho_pantalla = root.winfo_screenwidth()
altura_pantalla = root.winfo_screenheight()

# Calculamos la posición x e y para centrar la ventana
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (altura_pantalla // 2) - (altura_ventana // 2)

# Establecemos las dimensiones y la posición de la ventana
root.geometry('{}x{}+{}+{}'.format(ancho_ventana, altura_ventana, x, y))
root.title("CALCULO DE RED DE TUBERIAS")

#------------------
lbl_filas = tk.Label(root, text="TRAMO",font=("Arial", 10, "bold"))
lbl_filas.grid(row=1, column=2)
lbl_columnas = tk.Label(root, text="F",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=3)
lbl_columnas = tk.Label(root, text="L",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=4)
lbl_columnas = tk.Label(root, text="D",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=5)
lbl_columnas = tk.Label(root, text="Q",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=6)

lbl_columnas = tk.Label(root, text="CIRCUITO 1:",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=3, column=0)

# Crear una lista de listas de cajas de texto


cajas_texto = []
for i in range(4):
    fila_cajas_texto = []
    for j in range(5):
        if j==0:
            valor="AB"
        else:
            valor=0    
        caja_texto = tk.Entry(root,width=8)
        caja_texto.grid(row=i+2, column=j+2)
        caja_texto.insert(0, valor)
        fila_cajas_texto.append(caja_texto)
    cajas_texto.append(fila_cajas_texto)

lbl_filas = tk.Label(root, text="TRAMO",font=("Arial", 10, "bold"))
lbl_filas.grid(row=1, column=10)
lbl_columnas = tk.Label(root, text="F",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=11)
lbl_columnas = tk.Label(root, text="L",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=12)
lbl_columnas = tk.Label(root, text="D",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=13)
lbl_columnas = tk.Label(root, text="Q",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=14)
lbl_columnas2 = tk.Label(root, text="CIRCUITO 2:",font=("Arial", 10, "bold"))
lbl_columnas2.grid(row=3, column=7)

cajas_texto1 = []

for i in range(4):
    fila_cajas_texto = []
    a=8
    for j in range(5):
        if j==0:
            valor="AB"
        else:
            valor=0  
        caja_texto1 = tk.Entry(root,width=8)
        caja_texto1.grid(row=i+2, column=a+2)
        caja_texto1.insert(0, valor)
        fila_cajas_texto.append(caja_texto1)
        a+=1       
    cajas_texto1.append(fila_cajas_texto)



lbl_filas = tk.Label(root, text="TRAMO",font=("Arial", 10, "bold"))
lbl_filas.grid(row=1, column=17)
lbl_columnas = tk.Label(root, text="F",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=18)
lbl_columnas = tk.Label(root, text="L",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=19)
lbl_columnas = tk.Label(root, text="D",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=20)
lbl_columnas = tk.Label(root, text="Q",font=("Arial", 10, "bold"))
lbl_columnas.grid(row=1, column=21)
lbl_columnas2 = tk.Label(root, text="CIRCUITO 3:",font=("Arial", 10, "bold"))
lbl_columnas2.grid(row=3, column=15)    

cajas_texto3 = []

for i in range(4):
    fila_cajas_texto = []
    a=15
    for j in range(5):
        if j==0:
            valor="AB"
        else:
            valor=0  
        caja_texto3 = tk.Entry(root,width=8)
        caja_texto3.grid(row=i+2, column=a+2)
        caja_texto3.insert(0, valor)
        fila_cajas_texto.append(caja_texto3)
        a+=1       
    cajas_texto3.append(fila_cajas_texto)

# Crear un botón para imprimir los valores de las cajas de texto
def print_matrix(matrix):
  for row in matrix:
    for element in row:
      print(element, end='      ')
    print("")
  print("--------------------------------------------------------------------------")  

# EXPORTAR ARCHIVOS EN EXCEL
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


matriz = [["TRAMO   ","f   ", "L   ", "D   ","Q","     r","           rQ^2","              signo(rQ^2)","              |2rQ|","              Qr"], 
         ["AB",0.02, 800, 0.75,1,5,6,7,8,0], 
         ["BC",0.02, 850, 0.75,1,5,6,7,8,0], 
         ["CD",0.02, 850, 0.75,0.3,5,6,7,8,0],
         ["AD",0.02, 700, 0.75,-0.5,5,6,7,8,0],
         [0,0, 0, 0,0,0,0,0,0,0],
         [0,0, 0, 0,0,0,0,0,0,0]]

matriz2 = [["TRAMO2   ","f   ", "L   ", "D   ","Q","     r","           rQ^2","              signo(rQ^2)","              |2rQ|","              Qr"],
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

def imprimir_valores():
    a=1
    for i, fila_cajas_texto in enumerate(cajas_texto):
        fila_valores = []
        b=0
        
        for j, caja_texto in enumerate(fila_cajas_texto):
            
            valor = caja_texto.get()
            fila_valores.append(valor)
            if b>0:
             convert=float(valor)
             matriz[a][b]=convert
            else:
             matriz[a][b]=valor
            b+=1
        print(fila_valores)
        a+=1
    a=1
    for i, fila_cajas_texto in enumerate(cajas_texto1):
        fila_valores = []
        b=0
        
        for j, caja_texto1 in enumerate(fila_cajas_texto):
            
            valor = caja_texto1.get()
            fila_valores.append(valor)
            if b>0:
             convert=float(valor)
             matriz2[a][b]=convert
            else:
             matriz2[a][b]=valor
            b+=1
        print(fila_valores)
        a+=1
    a=1
    for i, fila_cajas_texto in enumerate(cajas_texto3):
        fila_valores = []
        b=0
        
        for j, caja_texto3 in enumerate(fila_cajas_texto):
            
            valor = caja_texto3.get()
            fila_valores.append(valor)
            if b>0:
             convert=float(valor)
             matriz3[a][b]=convert
            else:
             matriz3[a][b]=valor
            b+=1
        print(fila_valores)
        a+=1 
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
        






lbl_columnas3 = tk.Label(root, text="",font=("Arial", 10, "bold"))
lbl_columnas3.grid(row=8, column=3)  

boton_imprimir = tk.Button(root, text="CALCULAR", command=imprimir_valores)
boton_imprimir.grid(row=9, column=8, columnspan=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
