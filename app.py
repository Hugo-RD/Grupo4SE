import tkinter
from tkinter import filedialog
from ventanas_auxiliares import *
from regresion_lineal import *
from leer_archivos import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pickle

class Ventana_Principal(Ventana):
    def __init__(self):
        super().__init__(1000, 850, "Modelos de regresión lineal")
        self.frame_var = None  # Variable para el frame de variables
        self.var_guardado = None
        self.estado = False    #inhabilita boton de guardado
        self.variables = []    # Lista para almacenar las variables seleccionadas
        self.et_variables = tkinter.Label(self.frame_var, text="")

        self.escoger_archivo()  # Crear el primer frame
        self._save_load()       # Agregar botones de carga/guardado
        self.ventana.mainloop() # Iniciar la ventana

    def escoger_archivo(self):
        # Crear el primer frame de la ventana
        self.frame_base = tkinter.Frame(self.ventana)
        self.frame_base.pack()

        self.et_bienvenida = tkinter.Label(self.frame_base, text="\nBienvenido a la interfaz, escoja un archivo\n")
        self.et_bienvenida.pack()

        self.boton_escoger = tkinter.Button(self.frame_base, text="Escoger archivo",
                                            command=self.__escoger_archivo,
                                            bg="light grey", width=17, height=4)
        self.boton_escoger.pack()

        self.et_path = tkinter.Label(self.frame_base)
        self.et_path.pack()

    def __escoger_archivo(self):
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
    
            self.et_path.config(text=f"Archivo cargado: {ruta}", bg="light blue")

            if self.frame_var: #si habia otro archivo escogido antes
                self.frame_var.destroy()
            if hasattr(self, 'frame_mod'): #si habia un modelo cargado
                self.frame_mod.destroy()
            self.frame_variables()
        else:
            Ventana_Error("No se encontró\n ningún archivo")

    def frame_variables(self):
        # Crear el segundo frame de la interfaz para seleccionar variables
        self.frame_var = tkinter.Frame(self.ventana)
        self.frame_var.pack()

        titulo_var = tkinter.Label(self.frame_var, text="\nEscoja 2 variables\n")
        titulo_var.pack()

        var_list = diferenciar_variables(self.data)  # Buscar variables numéricas
        check_vars = []
        radio_var = tkinter.StringVar()  # Variable de control para los radiobuttons

        # Crear un marco para los checkboxes
        check_frame = tkinter.Frame(self.frame_var)
        check_frame.pack()

        # Crear checkboxes para cada variable y mostrarlos en horizontal
        for var in var_list:
            var_control = tkinter.IntVar()  # Crear una variable de control para el checkbox
            checkbox = tkinter.Checkbutton(check_frame, text=var, variable=var_control)
            checkbox.pack(side=tkinter.LEFT)  # Mostrar los checkboxes en horizontal
            check_vars.append((var, var_control))  # Almacenar el nombre de la variable y su variable de control

        # Crear un marco para los radiobuttons
        radio_frame = tkinter.Frame(self.frame_var)
        radio_frame.pack(pady=10)

        # Crear radiobuttons para cada opción en la segunda fila y mostrarlos en horizontal
        for var in var_list:
            radio_button = tkinter.Radiobutton(radio_frame, text=var, variable=radio_var, value=var)
            radio_button.pack(side=tkinter.LEFT)  # Mostrar los radiobuttons en horizontal

        self.boton_generar = tkinter.Button(self.frame_var, text="Generar Recta de Regresión",
                                            bg="light grey", width=25, height=2,
                                            command=lambda: self.generar_RR(check_vars, radio_var.get()))
        self.boton_generar.pack(pady=20)


    def generar_RR(self, vars, indp):
        cntx = sum(status.get() for _, status in vars)

        if cntx != 1:
            Ventana_Error("Debe seleccionar \nexactamente\n1 variable x")
        else:
            #actualizamos estado
            self.estado = True #habilita boton de guardado
            #buscamos variable seleccionada
            self.variables = [var_name for var_name, status in vars if status.get() == 1]

            m, corte_y, ec_recta, r_squared, mse, mae = regresion_lineal(self.data, self.variables[0], indp)

            #almacenamos las variables escogidas como un objeto modeloRR 
            self.var_guardado = ModeloRegresionLineal(self.variables[0], indp, ec_recta, r_squared, mse, mae)
            
            if hasattr(self, 'frame_var2'):
                self.frame_var2.destroy()

            self.frame_var2 = tkinter.Frame(self.frame_var)
            self.frame_var2.pack(pady=10)

            self.show_model(self.frame_var2, self.var_guardado, 33)
            
            # Eliminar el gráfico anterior si existe
            if hasattr(self, 'canvas_widget'):
                self.canvas_widget.destroy()

            # Crear un gráfico y mostrarlo en la misma ventana
            fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
            ax.scatter(self.data[self.variables[0]], self.data[indp], label="Datos reales")
            ax.plot(self.data[self.variables[0]], m * self.data[self.variables[0]] + corte_y, color='red', label="Predicciones")

            ax.set_xlabel(self.variables[0])
            ax.set_ylabel(indp)

            ax.legend()

            # Incorporar el gráfico en la interfaz
            canvas = FigureCanvasTkAgg(fig, master=self.frame_var)
            self.canvas_widget = canvas.get_tk_widget()
            self.canvas_widget.pack()

            # Cerrar la ventana de gráficos externa
            plt.close()
            
    def _save_load(self):
        frame_abajo = tkinter.Frame(self.ventana)
        frame_abajo.pack(side="bottom", pady=40)

        button_S = tkinter.Button(frame_abajo, text="Guardar modelo", bg="light grey",
                                width=17, height=4, command=lambda: self.save_RR())
        button_S.pack(side="left", padx=10)

        button_L = tkinter.Button(frame_abajo, text="Cargar modelo", bg="light grey",
                                width=17, height=4, command= lambda: self.load_RR())
        button_L.pack(side="right", padx=10)

    def save_RR(self):
        # da funcionalidad al boton de guardado
        if self.estado:

            file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

            if file_path: 
                with open(file_path, "wb") as archivo:
                    #guardamos las variables escogidas en archivo local
                    pickle.dump(self.var_guardado, archivo) 
            #print de confirmacion
            print(f"Datos guardados en {file_path}")
        else:
            Ventana_Error('No se creó un modelo')
    
    def load_RR(self):
        # Da funcionalidad al botón de carga
        file_path = filedialog.askopenfilename(defaultextension=".pkl", filetypes=[("Archivos pickle", "*.pkl")])

        if file_path:
            with open(file_path, "rb") as archivo:
                # Carga las variables desde el archivo local
                modelo = pickle.load(archivo)

            # Print de confirmación
            print(f"Datos cargados desde {file_path}")
            #mostrar ruta archivo cargado
            self.et_path.config(text=file_path, bg="light blue")
            self.load_frame(modelo) #creamos frame del modelo

    def load_frame(self, modelo):
        # Borramos el frame de variables si existe
        if self.frame_var:
            self.frame_var.destroy()
        # Borramos el frame de variables del modelo si existe
        if hasattr(self, 'frame_mod'):
            self.frame_mod.destroy()

        #actualizamos el estado
        self.estado = False # inhabilita el boton de guardado
        #creamos frame modelo
        self.frame_mod = tkinter.Frame(self.ventana)
        self.frame_mod.pack()

        exito = tkinter.Label(self.frame_mod, text="Se cargó el documento .pkl con éxito")
        exito.pack(pady=15)

        #se crea frame para las variables a cargar
        var_frame = tkinter.Frame(self.frame_mod)
        var_frame.pack(pady=25) 
        #creamos las etiquetas de las variables
        self.show_model(var_frame, modelo, 0)


    def show_model(self, frame, modelo, cnt):
        if cnt == 0: 
            #solo entra cuando se muestra un archivo cargado
            et_variables = tkinter.Label(frame, text=f"\nDatos: \nVariable X: {modelo.get_x()}, Variable Y: {modelo.get_y()}")
            et_variables.pack()
        et_recta = tkinter.Label(frame, text=f"Ecuación recta: {modelo.get_ecuacion_recta()}")
        et_errores = tkinter.Label(frame, text=f"Error cuadrático medio: {modelo.get_cuadratico()}, Error absoluto medio: {modelo.get_absoluto()}")
        et_coef = tkinter.Label(frame, text=f"Coeficiente R^2: {modelo.get_r_cuadrado()}")
        #las enseñamos
        
        et_recta.pack()
        et_errores.pack()
        et_coef.pack()

if __name__ == "__main__":
    Ventana_Principal()

