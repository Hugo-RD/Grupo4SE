import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import pickle
import pandas as pd
from guardar_cargar_archivos import save_RR
from regresion_lineal import ModeloRegresionLineal
from leer_archivos import leer_csv, leer_xlsx, leer_sql


class ModeloRegresionLinealTest(unittest.TestCase):

    def setUp(self):
        # Configuración común para las pruebas, si es necesario
        pass

    def tearDown(self):
        # Limpiar después de las pruebas, si es necesario
        pass

    def test_get_x(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_x(), 1)

    # Repite este patrón para cada método que desees probar

    def test_get_y(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_y(), 2)

    def test_get_ecuacion_recta(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_ecuacion_recta(), "y = mx + b")

    def test_coeficiente_r_cuadrado(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_r_cuadrado(), 0.9)
    
    def test_error_cuadratico(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_cuadratico(), 0.01)
    
    def test_error_absoluto(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_absoluto(), 0.1)
    
    def test_m(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_m(), 2)
    
    def test_n(self):
        instancia = ModeloRegresionLineal(x=1, y=2, ecuacion_recta="y = mx + b", coeficiente_r_cuadrado=0.9,
                             error_cuadratico=0.01, error_absoluto=0.1, m=2, n=3)
        self.assertEqual(instancia.get_n(), 3)

class TestLeerCSV(unittest.TestCase):
    def setUp(self):
        # Puedes establecer configuraciones iniciales o preparar datos de prueba aquí
        pass

    def test_leer_csv(self):
        # Define la ruta de un archivo CSV de prueba (asegúrate de que exista)
        csv_path = 'datos de ejemplo/housing.csv'

        # Llama a la función que deseas probar
        result = leer_csv(csv_path)

        # Asegúrate de que el resultado no sea nulo y sea del tipo esperado
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

class TestLeerXLSX(unittest.TestCase):
    def setUp(self):
        # Puedes establecer configuraciones iniciales o preparar datos de prueba aquí
        pass

    def test_leer_xlsx(self):
        # Define la ruta de un archivo de Excel de prueba (asegúrate de que exista)
        excel_path = 'datos de ejemplo/housing.xlsx'

        # Llama a la función que deseas probar
        result = leer_xlsx(excel_path)

        # Asegúrate de que el resultado no sea nulo y sea del tipo esperado
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

class TestLeerSQL(unittest.TestCase):
    def setUp(self):
        # Puedes establecer configuraciones iniciales o preparar datos de prueba aquí
        pass

    def test_leer_sql(self):
        # Define la ruta de un archivo de Excel de prueba (asegúrate de que exista)
        sql_path = 'datos de ejemplo/housing.sql'

        # Llama a la función que deseas probar
        result = leer_sql(sql_path)

        # Asegúrate de que el resultado no sea nulo y sea del tipo esperado
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

class TestSaveRR(unittest.TestCase):
    @patch("guardar_cargar_archivos.save_", return_value="mocked_file_path.pkl")
    @patch("builtins.open", create=True)
    @patch("pickle.dump")

    def test_save_RR(self, mock_dump, mock_open, mock_obtener_file_path):
        # Configurar el objeto ModeloRegresionLineal de prueba
        var_guardado = MagicMock()

        # Llamar a la función save_RR
        save_RR(var_guardado)

        # Verificar que la función obtener_file_path haya sido llamada
        mock_obtener_file_path.assert_called_once()

        # Verificar que la función open haya sido llamada con el archivo mock
        mock_open.assert_called_once_with("mocked_file_path.pkl", "wb")

        # Verificar que la función pickle.dump haya sido llamada con las variables correctas
        mock_dump.assert_called_once_with(var_guardado, mock_open.return_value.__enter__.return_value)


    
if __name__ == '__main__':
    unittest.main()