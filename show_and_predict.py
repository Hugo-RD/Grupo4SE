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

def show_preddict(frame, modelo, cnt):

    """etiqueta fran 1"""

    if cnt!=0: #solo entra con archivos no cargados
        et_showX = tkinter.Label(frame, text= f"Variable x: {modelo.get_x()}")
        et_showX.pack(pady=20)

        
    frame_pred = tkinter.Frame(frame)
    frame_pred.pack(pady=30)

    """etiqueta fran 2"""
    
    entry = tkinter.Entry(frame_pred, width=30)
    entry.pack(side=tkinter.RIGHT, padx=10)
    #con entry.get() se coge lo escrito

    """botón costo"""