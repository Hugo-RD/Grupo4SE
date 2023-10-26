import tkinter
from abrir_archivos import *
from tkinter import filedialog
from ventanas_auxiliares import Ventana_Error
from ventana_madre import *
from mostrar_variables import diferenciar_variables
from regresion_lineal import *


class Ventana_Principal(Ventana):
    def __init__(self):
        super().__init__(850, 850, "Modelos de regresión lineal")
        self.conf_archivo = False
        self.frame_var = False
        self.variables = False

        self.escoger_archivo() #creamos primer frame
        self._save_load() #botones de carga/guardado
        self.ventana.mainloop() #ejecutamos la ventana

    def escoger_archivo(self):
        #creamos el primer frame de la ventana
        self.frame_base = tkinter.Frame(self.ventana)
        self.frame_base.pack()

        self.espacio(self.frame_base)
        self.et_bienvenida = tkinter.Label(self.frame_base, text="Bienvenido a la interfaz, escoja un archivo")
        self.et_bienvenida.pack()
        self.boton_escoger = tkinter.Button(self.frame_base, text="Escoger archivo", 
                                command=lambda: self.__escoger_archivo(),
                                bg="light grey", width=17, height=4)
        self.boton_escoger.pack()

        self.et_path = tkinter.Label(self.frame_base)
        self.et_path.pack()
    
    def __escoger_archivo(self):
        #buscar archivo a cargar en la biblioteca
        ruta = tkinter.filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"),
                                                         ("Archivos Excel", "*.xlsx"),
                                                         ("Todos los archivos", "*.*")])
        if ruta:
            if ruta.lower().endswith(".csv"):
                self.data = leer_csv(ruta)    #CAMBIAR POR LECTURA CORRECTA
                self.conf_archivo = True
            elif ruta.lower().endswith(".xlsx"):
                self.data = leer_xlsx(ruta)   #CAMBIAR POR LECTURA CORRECTA
                self.conf_archivo = True
            else:
                Ventana_Error("El archivo introducido\n no es válido")
            self.et_path.config(text=f"Archivo cargado: {ruta}", bg="light blue")

            if self.frame_var:
                self.frame_var.destroy()
            self.frame_variables()
        else:
            Ventana_Error("No se encontró\n ningún archivo")

    def frame_variables(self):
        #crear 2 frame de la interfaz
        self.frame_var = tkinter.Frame(self.ventana)
        self.frame_var.pack()
        self.espacio(self.frame_var)
        titulo_var = tkinter.Label(self.frame_var, text="Escoja 2 variables")
        titulo_var.pack()
        self.espacio(self.frame_var)
        #buscar variables numéricas
        var_list = diferenciar_variables(self.data) #buscamos las variables numéricas
        check_vars = []
        for var in var_list:
            var_control = tkinter.IntVar()  # Crear una variable de control para el checkbox
            b = tkinter.Checkbutton(self.frame_var, text=var, variable=var_control)
            b.pack()
            check_vars.append((var, var_control))  # Almacenar el nombre de la variable y su variable de control
        
        #creamos boton para generar la RR
        self.espacio(self.frame_var)
        self.boton_generar = tkinter.Button(self.frame_var, text="Generar Recta de Regresión",
                                            bg="light grey", command=lambda: self.generar_RR(check_vars))
        self.boton_generar.pack()
        self.espacio(self.frame_var)
        self.et_info = tkinter.Label(self.frame_var, text="")
        self.et_info.pack()
        
    def generar_RR(self, vars):
        cnt = 0
        for _, status in vars:
            if status.get() == 1:  # Utiliza status.get() para verificar si el checkbox está seleccionado
                cnt += 1
        if cnt > 2:
            Ventana_Error("Introducidas más \nde 2 variables")
        elif cnt < 2:
            Ventana_Error("Introducidas menos \nde 2 variables")
        else:
            self.variables = []
            for var_name, status in vars:
                if status.get() == 1:  # Utiliza status.get() para verificar si el checkbox está seleccionado
                    self.variables.append(var_name)
            m, r_squared, mse, mae  = regresion_lineal(self.data, self.variables[0], self.variables[1])
            self.et_info.config(text=f"Datos: \n\nVariable X: {self.variables[0]}\nVariable Y: {self.variables[1]} \nPendiente: {m}\nError R^2: {r_squared}\nError cuadrático medio: {mse}\nError absoluto medio: {mae}")
    
    def _save_load(self):
        frame_abajo = tkinter.Frame(self.ventana)
        frame_abajo.pack(side="bottom", pady = 100)

        button_S = tkinter.Button(frame_abajo, text="Guardar modelo", bg="light grey",
                                width=17, height=4)
        button_S.pack(side="left", padx=10)
        button_L = tkinter.Button(frame_abajo, text="Cargar modelo", bg="light grey", 
                                width=17, height=4)
        button_L.pack(side="right", padx=10)
    
            



        

    def espacio(self, frame):
        espacio = tkinter.Label(frame, text="\n")
        espacio.pack()





if __name__ == "__main__":
    Ventana_Principal()