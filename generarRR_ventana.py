#nuestros archivos
from ventanas_auxiliares import Ventana_Error
from regresion_lineal import *
from show_and_predict import *
#otros
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def generar_RR(self, combo_x, combo_y):
        var_x = combo_x.get()
        var_y = combo_y.get()

        if var_x == "Seleccionar X" or var_y == "Seleccionar Y":
            Ventana_Error("Debe seleccionar dos variables para X e Y")
            return
        
        else:
            # Buscamos variable seleccionada
            self.variables = [var_x]

            m, corte_y, ec_recta, r_squared, mse, mae, n = regresion_lineal(self.data, var_x, var_y)

            # Almacenamos las variables escogidas como un objeto modeloRR
            self.var_guardado = ModeloRegresionLineal(var_x, var_y, ec_recta, r_squared, mse, mae, m, n)

            if hasattr(self, 'frame_var2'):
                self.frame_var2.destroy()

            self.frame_var2 = tkinter.Frame(self.frame_var)
            self.frame_var2.pack(pady=10)

            show_model(self.frame_var2, self.var_guardado, 33)

            # Eliminar el gráfico anterior si existe
            if hasattr(self, 'canvas_widget'):
                self.canvas_widget.destroy()

            # Crear un gráfico y mostrarlo en la misma ventana
            fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
            ax.scatter(self.data[var_x], self.data[var_y], label="Datos reales")
            ax.plot(self.data[var_x], m * self.data[var_x] + corte_y, color='red', label="Predicciones")

            ax.set_xlabel(var_x)
            ax.set_ylabel(var_y)

            ax.legend()

            # Incorporar el gráfico en la interfaz
            canvas = FigureCanvasTkAgg(fig, master=self.frame_var)
            self.canvas_widget = canvas.get_tk_widget()
            self.canvas_widget.pack()

            # Cerrar la ventana de gráficos externa
            plt.close()

            # Opción a hacer una predicción
            show_preddict(self.frame_var2, self.var_guardado)

            # Habilitar el botón "Guardar modelo" después de generar un modelo
            self.button_S['state'] = 'normal'
      