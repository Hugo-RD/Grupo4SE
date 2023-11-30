import tkinter

def show_model(frame, modelo, cnt):   
  
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


def show_preddict(frame, modelo):

    """etiqueta fran 1"""
    frame_pred = tkinter.Frame(frame)
    frame_pred.pack(pady=30)
    et_showX = tkinter.Label(frame_pred, text= f"Predicciones")
    et_showX.pack(pady=20)
    
    et_showX.config(text= f"Predicciones: Variable x: {modelo.get_x()}")

    """etiqueta fran 2"""
    et_recta = tkinter.Label(frame_pred, text=f"Ecuación recta: {modelo.get_ecuacion_recta()}")
    et_recta.pack(side=tkinter.LEFT)
    entry = tkinter.Entry(frame_pred, width=30)
    entry.pack(side=tkinter.LEFT, padx=10)
    #con entry.get() se coge lo escrito
    btn_generar_prediccion = tkinter.Button(frame_pred, text="Generar Predicción", command=lambda: calcular_y(modelo,entry,resultado_label))
    btn_generar_prediccion.pack(side=tkinter.LEFT, padx=10)
    
    resultado_label = tkinter.Label(frame_pred, text="Resultado: ")
    resultado_label.pack(side=tkinter.LEFT, padx=10)

    """botón costo"""
 

def calcular_y(modelo, entry, resultado_label):
    try:
        x_value = float(entry.get())
        y = float(modelo.get_m()) * x_value + float(modelo.get_n())
        resultado_label.config(text=f"Resultado: {y}")
    except ValueError:
        resultado_label.config(text="Error: Ingresa un valor válido para X")
    