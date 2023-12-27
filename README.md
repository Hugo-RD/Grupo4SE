## Creación, guardado y carga de modelos de regresión lineal

La aplicación permite representar modelos de regresión lineal a partir de bases de datos introducidas por el usuario y hacer predicciones. Tan solo necesitarás ejecutar el código y elegir en la interfaz las variables a contrastar. Además, podrás guardar modelos en local y cargarlos.

#### Pasos para la instalación:
- En GitHub, ve al apartado de Tags
- Accede a Releases
- Descarga la carpeta .zip.
- Ejecuta el módulo app en la consola o en un intérprete de Python.
- Ejecuta la aplicación y disfruta.
 **NOTA**: Si no se dispone de alguna de las siguientes librerías es neesario instalarla: Tkinter, Pickle, Sklearn, Matplotlib, Numpy, Pandas, Sqlite3.
#### Guía de uso:
Puedes disfrutar de la aplicación tanto desde consola como desde un intérprete de Python.
Para comenzar en consola, una vez hayas instalado Python y estés en el directorio donde se encuentre la carpeta correspondiente al proyecto , 
debes ejecutar python3 run app.py.
Para hacerlo en un intérprete de Python, debes ejecutar el código del módulo app.py
Después de haber realizado una de las opciones anteriores, debes seleccionar mediante la interfaz el archivo del que se estudiarán los datos.
A continuación, podrás seleccionar las variables "x" e "y" entre todas las posibles para realizar un modelo de regresión lineal ; 
o bien cargar un modelo ya creado y guardado con anterioridad. 
Selecciones una u otra opción , se mostrarán por pantalla los datos correspondientes al modelo. 

Para realizar predicciones del valor de la variable "y", debes introducir un valor positivo en la celda correspondiente a predicciones y hacer clic sobre el botón "generar predicción".

##### Paso a paso con imágenes:
- Ejecuta app.py en tu intérprete

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/vetanaapp.PNG)

- En la ventana que se mostrará por pantalla, haz clic en el botón de "Escoger archivo"

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/interfaz1.PNG)

- Selecciona el formato de archivo que desees entre los disponibles, y a continuación el archivo cuyos datos quieras tratar.

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/seleccionarchivo.PNG)

- Se verá lo siguiente en la ventana, en la que deberás seleccionar las variables y hacer clic en el botón de "Generar Recta de Regresión"

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/seleccionarvariables.PNG)

- Se mostrarán los datos y gráfica correspondientes al modelo.

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/datosgrafica.PNG)

- Para generar una predicción, solo debes introducir una cantidad correspondiente a la variable x y hacer clic en el botón de  "Generar predicción"

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/prediccion.PNG)

- Si deseas, puedes guardar en local el modelo creado haciendo clic en el botón de "Guardar modelo".

![](https://github.com/Hugo-RD/Grupo4SE/blob/master/Imagenes/guardarmodelo.PNG)

- Estos mismos podrán cargarse haciendo clic en el botón "Cargar modelo".



#### Creado con:
- Python
