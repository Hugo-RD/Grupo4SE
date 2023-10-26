from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

def regresion_lineal(data, var1, var2):
    data = data.dropna() #quitamos los NaN
    X = np.array(data[var1]).reshape(-1, 1)
    y = np.array(data[var2])
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    plt.scatter(X, y, label="Datos reales")
    plt.plot(X, y_pred, color='red', label="Predicciones")
    
    # Personalizar los títulos de los ejes
    plt.xlabel(var1)
    plt.ylabel(var2)
    
    plt.legend()
    plt.show()


    r_squared = model.score(X, y)  # R^2
    mse = mean_squared_error(y, y_pred)  # Error cuadrático medio
    mae = mean_absolute_error(y, y_pred)  # Error absoluto medio
    return model.coef_[0], r_squared, mse, mae  # Obtenemos la pendiente
