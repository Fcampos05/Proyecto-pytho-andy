import tkinter as tk

def create_table():
    # Obtener el número de filas y columnas desde los campos de texto
    rows = int(entry_rows.get())
    columns = int(entry_columns.get())


    # Crear las cabeceras
    for col in range(columns):
        label = tk.Label(container, text=f"Columna {col + 1}")
        label.grid(row=0, column=col)

    # Crear los campos de texto dinámicamente
    for row in range(1, rows + 1):
        for col in range(columns):
            entry = tk.Entry(container)
            entry.grid(row=row, column=col)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario dinámico")

# Crear los campos de texto para ingresar el número de filas y columnas
entry_rows = tk.Entry(root)
entry_rows.pack()

entry_columns = tk.Entry(root)
entry_columns.pack()

# Crear el botón para generar la tabla
button = tk.Button(root, text="Generar tabla", command=create_table)
button.pack()

# Crear el contenedor para la tabla
container = tk.Frame(root)
container.pack()

# Mostrar la ventana principal
root.mainloop()
