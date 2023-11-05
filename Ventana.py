import tkinter
from tkinter import filedialog
from ventanas_auxiliares import Ventana_Error
from ventana_madre import Ventana
from mostrar_variables import diferenciar_variables
from regresion_lineal import *
from abrir_archivos import *

class Ventana_Principal(Ventana):
    def __init__(self):
        super().__init__(850, 850, "Modelos de regresión lineal")
        self.frame_var = None  # Variable para el frame de variables
        self.variables = []    # Lista para almacenar las variables seleccionadas

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

            if self.frame_var:
                self.frame_var.destroy()
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

        for var in var_list:
            var_control = tkinter.IntVar()  # Crear una variable de control para el checkbox
            b = tkinter.Checkbutton(self.frame_var, text=var, variable=var_control)
            b.pack()
            check_vars.append((var, var_control))  # Almacenar el nombre de la variable y su variable de control

        self.boton_generar = tkinter.Button(self.frame_var, text="Generar Recta de Regresión",
                                            bg="light grey", command=lambda: self.generar_RR(check_vars))
        self.boton_generar.pack()

        self.et_cortes = tkinter.Label(self.frame_var, text="")
        self.et_variables = tkinter.Label(self.frame_var, text="")
        self.et_recta = tkinter.Label(self.frame_var, text="")
        self.et_errores = tkinter.Label(self.frame_var, text="")

        self.et_variables.pack()
        self.et_recta.pack()
        self.et_cortes.pack()
        self.et_errores.pack()

    def generar_RR(self, vars):
        cnt = sum(status.get() for _, status in vars)

        if cnt != 2:
            Ventana_Error("Debe seleccionar exactamente 2 variables")
        else:
            #estamos cogiendo siempre como var X la que esté más arriba en el orden de seleccion
            self.variables = [var_name for var_name, status in vars if status.get() == 1]
            m, corte_x, corte_y, ec_recta, r_squared, mse, mae = regresion_lineal(self.data, self.variables[0], self.variables[1])

            self.et_variables.config(text=f"\nDatos: \nVariable X: {self.variables[0]}, Variable Y: {self.variables[1]}")
            self.et_recta.config(text=f"Ecuación recta: {ec_recta}, Pendiente: {m}")
            self.et_cortes.config(text=f"Corte eje X: {corte_x}, Corte eje Y: {corte_y}")
            self.et_errores.config(text=f"Error R^2: {r_squared}, Error cuadrático medio: {mse}, Error absoluto medio: {mae}")

    def _save_load(self):
        frame_abajo = tkinter.Frame(self.ventana)
        frame_abajo.pack(side="bottom", pady=100)

        button_S = tkinter.Button(frame_abajo, text="Guardar modelo", bg="light grey",
                                width=17, height=4)
        button_S.pack(side="left", padx=10)

        button_L = tkinter.Button(frame_abajo, text="Cargar modelo", bg="light grey",
                                width=17, height=4)
        button_L.pack(side="right", padx=10)

if __name__ == "__main__":
    Ventana_Principal()
