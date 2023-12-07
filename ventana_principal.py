import tkinter
from tkinter import ttk, filedialog
from sklearn.metrics import mean_squared_error, mean_absolute_error

"""nuestros archivos"""
from show_and_predict import *
from ventanas_auxiliares import *
from regresion_lineal import *
from leer_archivos import *
from guardar_cargar_archivos import *
from generarRR_ventana import *
from escoger_arch_ventana import *

class Ventana_Principal(Ventana):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto, "Modelos de regresión lineal")
        self.frame_var = None  # Variable para el frame de variables
        self.var_guardado = None
        self.estado = False    #inhabilita boton de guardado
        self.variables = []    # Lista para almacenar las variables seleccionadas
        self.et_variables = tkinter.Label(self.frame_var, text="")

        escoger_archivo(self)  # Crear el primer frame
        self._save_load()       # Agregar botones de carga/guardado
        self.ventana.mainloop() # Iniciar la ventana

    def frame_variables(self):
        # Crear el segundo frame de la interfaz para seleccionar variables
        self.frame_var = tkinter.Frame(self.ventana)
        self.frame_var.pack()

        var_list = diferenciar_variables(self.data)  # Buscar variables numéricas
        
        # Combobox para la variable X
        combo_x = ttk.Combobox(self.frame_var, values=var_list, state="readonly", width=16)
        combo_x.set("Seleccionar X")
        combo_x.pack(side=tkinter.LEFT, padx=5, pady=15)

        # Combobox para la variable Y
        combo_y = ttk.Combobox(self.frame_var, values=var_list, state="readonly", width=16)
        combo_y.set("Seleccionar Y")
        combo_y.pack(side=tkinter.LEFT, padx=5, pady=15)

        self.boton_generar = tkinter.Button(self.frame_var, text="Generar Recta de Regresión",
                                            bg="light grey", width=21, height=0,
                                            command=lambda: generar_RR(self, combo_x, combo_y))

        self.boton_generar.pack(side=tkinter.LEFT, padx=5, pady=15)

        # Deshabilitar el botón inicialmente
        self.boton_generar['state'] = 'disabled'

        self.boton_generar.pack(side=tkinter.LEFT, padx=5, pady=15)

        # Verificar si se han seleccionado dos variables antes de habilitar el botón
        def verificar_seleccion():
            if combo_x.get() != "Seleccionar X" and combo_y.get() != "Seleccionar Y":
                self.boton_generar['state'] = 'normal'
            else:
                self.boton_generar['state'] = 'disabled'

        # Vincular la función de verificación a los Combobox
        combo_x.bind("<<ComboboxSelected>>", lambda event: verificar_seleccion())
        combo_y.bind("<<ComboboxSelected>>", lambda event: verificar_seleccion())

          
    def _save_load(self):
        #frame boton de carga
        frame_abajo = tkinter.Frame(self.ventana)
        frame_abajo.pack(side="bottom", pady=40)

        button_L = tkinter.Button(frame_abajo, text="Cargar modelo", bg="light grey",
                                width=17, height=2, command= lambda: load_RR(self))
        button_L.pack(side="right", padx=10, pady=15)

        #necesitamos que esté con self para poder deshabilitarlo
        self.button_S = tkinter.Button(frame_abajo, text="Guardar modelo", bg="light grey",
                                       width=17, height=2, command=lambda: save_RR(self.var_guardado))
        self.button_S.pack(side="right", padx=10, pady=15)

        # Deshabilitar el botón al inicio
        self.button_S['state'] = 'disabled'

    def load_frame(self, modelo):
        #deshabilitar el boton de guardado
        self.button_S['state'] = 'disabled'
        # Borramos el frame de variables si existe
        if self.frame_var:
            self.frame_var.destroy()
        # Borramos el frame de variables del modelo si existe
        if hasattr(self, 'frame_mod'):
            self.frame_mod.destroy()

        # Eliminar widgets del frame base (excepto el botón de escoger archivo)
        for widget in self.frame_base.winfo_children():
            if widget != self.boton_escoger and widget != self.et_path:
                widget.destroy()
                
        
        #creamos frame modelo
        self.frame_mod = tkinter.Frame(self.ventana)
        self.frame_mod.pack()

        exito = tkinter.Label(self.frame_mod, text="Se cargó el documento .pkl con éxito")
        exito.pack(pady=15)

        #se crea frame para las variables a cargar
        var_frame = tkinter.Frame(self.frame_mod)
        var_frame.pack(pady=25) 
        #creamos las etiquetas de las variables
        show_model(var_frame, modelo, 0)
        show_preddict(var_frame, modelo)


if __name__ == "__main__":
    Ventana_Principal(1000, 800)