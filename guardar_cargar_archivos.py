from tkinter import ttk, filedialog
import pickle

def save_RR(var_guardado):   ####REALIZAR PRUEBAS UNITARIAS
    """
    Guarda un modelo de regresión lineal en un archivo pickle.

    Args:
        var_guardado: Instancia de la clase ModeloRegresionLineal que se va a guardar.
    """
    # Da funcionalidad al botón de guardado
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

    if file_path: 
        with open(file_path, "wb") as archivo:
            # Guarda las variables escogidas en un archivo local usando pickle
            pickle.dump(var_guardado, archivo) 
    # Imprime confirmación
    print(f"Datos guardados en {file_path}")

def load_RR(self):
    """
    Carga un modelo de regresión lineal desde un archivo pickle y actualiza la interfaz gráfica.

    Args:
        self: Instancia de la clase Ventana_Principal.
    """
    # Da funcionalidad al botón de carga
    file_path = filedialog.askopenfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

    if file_path:
        with open(file_path, "rb") as archivo:
            # Carga las variables desde el archivo local
            modelo = pickle.load(archivo)

        # Muestra la ruta del archivo cargado
        self.et_path.config(text=f"Archivo cargado: {file_path}", bg="light blue")
        self.et_path.pack_configure(pady=15)

        # Crea el frame del modelo cargado
        self.load_frame(modelo)
