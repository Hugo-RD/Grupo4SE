from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

def regresion_lineal(data, var1, var2):
    data = data.dropna()  # Quitamos los NaN
    X = np.array(data[var1]).reshape(-1, 1)
    y = np.array(data[var2])
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    """
    #si quisisesemos enseñarlo en otra pestaña
    plt.scatter(X, y, label="Datos reales")
    plt.plot(X, y_pred, color='red', label="Predicciones")

    # Personalizar los títulos de los ejes
    plt.xlabel(var1)
    plt.ylabel(var2)

    plt.legend()
    plt.show()
    """

    r_squared = model.score(X, y)  # R^2
    mse = mean_squared_error(y, y_pred)  # Error cuadrático medio
    mae = mean_absolute_error(y, y_pred)  # Error absoluto medio

    # Coeficientes de la recta
    pendiente = model.coef_[0]
    ordenada_al_origen = model.intercept_

    # Puntos de corte con los ejes
    punto_de_corte_y = ordenada_al_origen

    # Ecuacon de la recta
    ecuacion_recta = f"y = {pendiente}x + {ordenada_al_origen}"

    return pendiente, punto_de_corte_y, ecuacion_recta, r_squared, mse, mae

class ModeloRegresionLineal:
    def __init__(self, x, y, ecuacion_recta, coeficiente_r_cuadrado, error_cuadratico, error_absoluto):
        self._x = x
        self._y = y
        self._ecuacion_recta = ecuacion_recta
        self._coeficiente_r_cuadrado = coeficiente_r_cuadrado
        self._error_cuadratico = error_cuadratico
        self._error_absoluto = error_absoluto
    
    def get_x(self):
        return self._x 
    
    def get_y(self):
        return self._y

    def get_ecuacion_recta(self):
        return self._ecuacion_recta
    
    def get_r_cuadrado(self):
        return self._coeficiente_r_cuadrado
    
    def get_cuadratico(self):
        return self._error_cuadratico
    
    def get_absoluto(self):
        return self._error_absoluto
        