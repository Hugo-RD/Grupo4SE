import tkinter 
#nuestro
from leer_archivos import *
from ventanas_auxiliares import Ventana_Error

def escoger_archivo(self):
    # Crear el primer frame de la ventana
    self.frame_base = tkinter.Frame(self.ventana)
    self.frame_base.pack()

    self.boton_escoger = tkinter.Button(self.frame_base, text="Escoger archivo",
                                        command=lambda:__escoger_archivo(self),
                                        bg="light grey", width=17, height=0)
    
    self.boton_escoger.pack(side=tkinter.LEFT, padx=5, pady=15)

    self.et_path = tkinter.Label(self.frame_base)
    self.et_path.pack()
    

def __escoger_archivo(self):
    # Eliminar widgets del frame base (excepto el botón de escoger archivo)
    for widget in self.frame_base.winfo_children():
        if widget != self.boton_escoger and widget != self.et_path:
            widget.destroy()
    # Buscar archivo a cargar en la biblioteca
    ruta = tkinter.filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"),
                                                            ("Archivos Excel", "*.xlsx"),
                                                            ("Archivos SQL", "*.db"),
                                                            ("Todos los archivos", "*.*")])
    if ruta:
        if ruta.lower().endswith(".csv"):
            self.data = leer_csv(ruta)
        elif ruta.lower().endswith(".xlsx"):
            self.data = leer_xlsx(ruta)
        elif ruta.lower().endswith(".db"):
            self.data = leer_sql(ruta)
        else:
            Ventana_Error("El archivo introducido\n no es válido")
            return

        self.et_path.config(text=f"Archivo cargado: {ruta[:50]}...", bg="light blue")
        self.et_path.pack_configure(side=tkinter.LEFT, padx= 5, pady=15)

        if self.frame_var: #si habia otro archivo escogido antes
            self.frame_var.destroy()
        if hasattr(self, 'frame_mod'): #si habia un modelo cargado
            self.frame_mod.destroy()
        self.frame_variables()
    else:
        Ventana_Error("No se encontró\n ningún archivo")
