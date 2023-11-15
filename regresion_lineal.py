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

