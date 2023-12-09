import tkinter 
# Nuestros archivos
from leer_archivos import *
from ventanas_auxiliares import Ventana_Error

def escoger_archivo(self):
    """
    Crea el primer frame de la ventana para escoger un archivo.

    Args:
        self: Instancia de la clase Ventana_Principal.
    """
    # Crear el primer frame de la ventana
    self.frame_base = tkinter.Frame(self.ventana)
    self.frame_base.pack()

    # Botón para escoger un archivo
    self.boton_escoger = tkinter.Button(self.frame_base, text="Escoger archivo",
                                        command=lambda: __escoger_archivo(self),
                                        bg="light grey", width=17, height=0)
    
    self.boton_escoger.pack(side=tkinter.RIGHT, padx=5, pady=15)

    # Etiqueta para mostrar la ruta del archivo seleccionado
    self.et_path = tkinter.Label(self.frame_base)
    self.et_path.pack()

def __escoger_archivo(self):
    """
    Función interna para manejar la selección de un archivo y cargarlo en la interfaz.

    Args:
        self: Instancia de la clase Ventana_Principal.
    """
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
        # Seleccionar la función de lectura según la extensión del archivo
        if ruta.lower().endswith(".csv"):
            self.data = leer_csv(ruta)
        elif ruta.lower().endswith(".xlsx"):
            self.data = leer_xlsx(ruta)
        elif ruta.lower().endswith(".db"):
            self.data = leer_sql(ruta)
        else:
            # Mostrar un mensaje de error si el archivo no es válido
            Ventana_Error("El archivo introducido no es válido")
            return

        # Mostrar la ruta del archivo cargado
        self.et_path.config(text=f"Archivo cargado: {ruta}", bg="light blue")
        self.et_path.pack_configure(side=tkinter.LEFT, padx=5, pady=15)

        # Eliminar el frame de variables anterior si existe
        if self.frame_var:
            self.frame_var.destroy()
        # Eliminar el frame de modelo anterior si existe
        if hasattr(self, 'frame_mod'):
            self.frame_mod.destroy()
        
        # Crear el segundo frame de la interfaz para seleccionar variables
        self.frame_variables()
    else:
        # Mostrar un mensaje de error si no se encuentra ningún archivo
        Ventana_Error("No se encontró ningún archivo")
