import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def seleccionar_csv():
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo CSV", 
        filetypes=[("Archivos CSV", "*.csv"), ("Todos", "*.*")])
    if ruta:
        entrada_csv.set(ruta)

def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    if ruta:
        entrada_carpeta.set(ruta)

def convertir():
    csv = entrada_csv.get().strip()
    carpeta = entrada_carpeta.get().strip()

    if not csv or not carpeta:
        messagebox.showerror("Error", "Por favor, selecciona un archivo CSV y una carpeta de destino.")
        return
    
    try:
        os.makedirs(carpeta, exist_ok=True)
        df = pd.read_csv(csv)
        nombre = os.path.splitext(os.path.basename(csv))[0]
        destino = os.path.join(carpeta, f"{nombre}.xlsx")
        df.to_excel(destino, index=False)
        lbl_estado.config(text=f"Archivo convertido exitosamente: {destino}", fg="green")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al convertir el archivo: {e}")
        lbl_estado.config(text="Error al convertir el archivo.", fg="red")

###
# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("CSV to Excel")
ventana.geometry("500x240")
ventana.resizable(False, False)

entrada_csv = tk.StringVar()
entrada_carpeta = tk.StringVar()

pad = {"padx": 16, "pady": 6}

tk.Label(ventana, text="Archivo CSV:").grid(row=0, column=0, sticky="e", **pad)
tk.Entry(ventana, textvariable=entrada_csv, width=40).grid(row=0, column=1, padx=16, pady=6)
tk.Button(ventana, text="Seleccionar", command=seleccionar_csv).grid(row=0, column=2, padx=16, pady=6)

tk.Label(ventana, text="Carpeta de destino:").grid(row=1, column=0, sticky="e", **pad)
tk.Entry(ventana, textvariable=entrada_carpeta, width=40).grid(row=1, column=1, padx=16, pady=6)
tk.Button(ventana, text="Seleccionar", command=seleccionar_carpeta).grid(row=1, column=2, padx=16, pady=6)

tk.Button(ventana, text="Convertir", command=convertir, bg="#534AB7", fg="white", padx=16, pady=6).grid(row=2, column=1, pady=10)

lbl_estado = tk.Label(ventana, text="", font=("", 10))
lbl_estado.grid(row=3, column=0, columnspan=3, pady=10)

ventana.mainloop()