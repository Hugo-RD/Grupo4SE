from tkinter import ttk, filedialog
import pickle


def save_RR(var_guardado):
    # da funcionalidad al boton de guardado
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

    if file_path: 
        with open(file_path, "wb") as archivo:
            #guardamos las variables escogidas en archivo local
            pickle.dump(var_guardado, archivo) 
    #print de confirmacion
    print(f"Datos guardados en {file_path}")


def load_RR(self):
    # Da funcionalidad al botón de carga
    file_path = filedialog.askopenfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

    if file_path:
        with open(file_path, "rb") as archivo:
            # Carga las variables desde el archivo local
            modelo = pickle.load(archivo)

        
        #mostrar ruta archivo cargado
        self.et_path.config(text=f"Archivo cargado: {file_path}", bg="light blue")
        self.et_path.pack_configure(pady=15)

        self.load_frame(modelo) #creamos frame del modelo
