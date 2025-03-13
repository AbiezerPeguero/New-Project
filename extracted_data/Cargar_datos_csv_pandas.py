import pandas as pd

# Cargar el archivo CSV
csv_file = "extracted_data/loan.csv"
df = pd.read_csv(
    csv_file, low_memory=False
)  # low_memory=False evita advertencias de tipos de datos

# Mostrar las primras 5 filas
print(df.head())

# Mostrar información sobre las columnas (para ver tipos de datos y valores nulos)
print(df.info())

# Mostrar nombres de todas las columnas
print(df.columns)
