import PySimpleGUI as sg
import pandas as pd
import os

# Tema visual
sg.theme("DarkBlue14")

layout = [

    [sg.Text(
        "Conversor CSV a Excel",
        font=("Segoe UI", 16, "bold"),
        justification="center",
        expand_x=True
    )],

    [sg.HorizontalSeparator()],

    [
        sg.Text("Archivo CSV:",font=("Segoe UI", 11), size=(18, 1), justification="right"),
        
        sg.Input(
            key="-CSV-",
            expand_x=True
        ),

        sg.FileBrowse(
            "Seleccionar",
            file_types=(("Archivos CSV", "*.csv"), ("Todos", "*.*"))
        )
    ],

    [
        sg.Text("Carpeta destino:",font=("Segoe UI", 11), size=(18, 1), justification="right"),

        sg.Input(
            key="-CARPETA-",
            expand_x=True
        ),

        sg.FolderBrowse("Seleccionar")
    ],

    [sg.Push(),

     sg.Button(
            "Convertir a Excel",
            key="-CONVERTIR-",
            size=(20, 1),
            font=("Segoe UI", 11, "bold"),
            button_color=("white", "#4F46E5"),
            border_width=0,
            mouseover_colors=("#FFFFFF", "#6366F1")
        ),

     sg.Push()]
]

ventana = sg.Window(
    "CSV to Excel",
    layout,
    size=(700, 220),
    resizable=False,
    margins=(20, 20)
)

while True:
    evento, valores = ventana.read()
    
    if evento in (None, "Cancelar"):
        break
    
    if evento == "-CONVERTIR-":
        csv_path = valores["-CSV-"].strip()
        carpeta = valores["-CARPETA-"].strip()
        
        if not csv_path or not carpeta:
            sg.PopupOK("Por favor, selecciona un archivo CSV y una carpeta de destino.", title="Error")
            continue
        
        try:
            os.makedirs(carpeta, exist_ok=True)
            df = pd.read_csv(csv_path)
            nombre = os.path.splitext(os.path.basename(csv_path))[0]
            destino = os.path.join(carpeta, f"{nombre}.xlsx")
            df.to_excel(destino, index=False)
            sg.PopupOK("Archivo convertido correctamente!", title="Éxito")
        except Exception as e:
            sg.PopupOK(f"Ocurrió un error al convertir el archivo:\n{e}", title="Error")

ventana.close()