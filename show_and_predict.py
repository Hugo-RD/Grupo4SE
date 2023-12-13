import tkinter

def show_model(frame, modelo):        
    """
    Muestra información sobre el modelo de regresión en una interfaz gráfica.

    Args:
        frame (tkinter.Frame): Frame en el que se mostrará la información.
        modelo: Modelo de regresión.
        cnt (int): Contador.
    """
    et_recta = tkinter.Label(frame, text=f"Ecuación recta: {modelo.get_ecuacion_recta()}")
    et_errores = tkinter.Label(frame, text=f"Error cuadrático medio: {modelo.get_cuadratico()}, Error absoluto medio: {modelo.get_absoluto()}")
    et_coef = tkinter.Label(frame, text=f"Coeficiente R^2: {modelo.get_r_cuadrado()}")
    
    # Mostrar etiquetas
    et_recta.pack()
    et_errores.pack()
    et_coef.pack()

def show_preddict(frame, modelo):
    """
    Muestra predicciones en una interfaz gráfica.

    Args:
        frame (tkinter.Frame): Frame en el que se mostrarán las predicciones.
        modelo: Modelo de regresión.
    """
    # Etiqueta para mostrar predicciones
    frame_pred = tkinter.Frame(frame)
    frame_pred.pack(pady=30)
    et_showX = tkinter.Label(frame_pred, text="Predicciones")
    et_showX.pack(pady=20)
    
    et_showX.config(text=f"Predicciones: Variable x: {modelo.get_x()}")

    # Entry para ingresar el valor de x
    entry = tkinter.Entry(frame_pred, width=30)
    entry.pack(side=tkinter.LEFT, padx=10)
    
    # Botón para generar predicción
    btn_generar_prediccion = tkinter.Button(frame_pred, text="Generar Predicción", command=lambda: calcular_y(modelo, entry, resultado_label))
    btn_generar_prediccion.pack(side=tkinter.LEFT, padx=10)
    
    # Etiqueta para mostrar el resultado de la predicción
    resultado_label = tkinter.Label(frame_pred, text=f"{modelo.get_y()} =")
    resultado_label.pack(side=tkinter.LEFT, padx=10)

def calcular_y(modelo, entry, resultado_label):
    """
    Calcula la predicción y muestra el resultado en una etiqueta.

    Args:
        modelo: Modelo de regresión.
        entry (tkinter.Entry): Entrada que contiene el valor de x.
        resultado_label (tkinter.Label): Etiqueta donde se mostrará el resultado.
    """
    try:
        x_value = float(entry.get())
        y = float(modelo.get_m()) * x_value + float(modelo.get_n())
        resultado_label.config(text=f"{modelo.get_y()}= {y}")
    except ValueError:
        resultado_label.config(text="Error: Ingresa un valor válido para X")
