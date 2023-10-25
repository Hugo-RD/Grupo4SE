import pandas as pd
from abrir_archivos import *

def escoger_variables(data):
    cnt = 1
    print('Escoja dos variables para crear un modelo de regresión lineal:')
    variables_num = diferenciar_variables(data)
    for variable in variables_num:
        print('Opción',cnt,':',variable)
        cnt += 1

def diferenciar_variables(data):
    variables_num = []
    for columna in data.columns:
        if pd.api.types.is_numeric_dtype(data[columna]):
            variables_num.append(columna)
    
    return variables_num

def guardar_variables(var_l):
    num = [1,2,3,4,5,6,7,8,9]
    v1= input("escoja la primera variable")
    while v1 not in num or v1 not in var_l:
        v1= input("escoja la primera variable")
    v2 = input("escoja la segunda variable")
    while v2 not in num or v2 not in var_l or v1 == v2:
        v2 = input("escoja la segunda variable")   

if __name__ == "__main__":
    data1=leer_csv("housing.csv")
    data2=leer_xlsx("housing.xlsx")
    print(data1.head())
    print()
    print(data2.head())
    escoger_variables(data1)
    escoger_variables(data2)
    print()
    print(diferenciar_variables(data1))
    print()
    print(diferenciar_variables(data2))
    
