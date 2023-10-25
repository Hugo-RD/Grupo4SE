import pandas as pd

def leer_csv(path):
    data = pd.read_csv(path, delimiter=',', header=0)
    return data
        
def leer_xlsx(path):
    data = pd.read_excel(path)
    return data

#pruebas
if __name__ == "__main__":
    data1=leer_csv("housing.csv")
    data2=leer_xlsx("housing.xlsx")
    print(data1.head())
    print()
    print(data2.head())
    print()
    print(data1.columns) #enseña las cabeceras