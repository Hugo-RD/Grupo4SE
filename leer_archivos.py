import pandas as pd
import sqlite3

def leer_csv(path): ####REALIZAR PRUEBAS UNITARIAS
    data = pd.read_csv(path, delimiter=',', header=0)
    return data
        
def leer_xlsx(path):   ####REALIZAR PRUEBAS UNITARIAS
    data = pd.read_excel(path)
    return data

def leer_sql(path):    ####REALIZAR PRUEBAS UNITARIAS
    conn = sqlite3.connect(path)
    data = pd.read_sql_query("SELECT * FROM california_housing_dataset", conn)
    conn.close()
    return data

def diferenciar_variables(data):
    variables_num = []
    for columna in data.columns:
        if pd.api.types.is_numeric_dtype(data[columna]):
            variables_num.append(columna)
    
    return variables_num

#pruebas
if __name__ == "__main__":
    data1=leer_csv("housing.csv")
    data2=leer_xlsx("housing.xlsx")
    data3=leer_sql("housing.db")
    print(data1.head())
    print()
    print(data2.head())
    print()
    print(data3.head())
    print()
    print(data1.columns) #enseña las cabeceras