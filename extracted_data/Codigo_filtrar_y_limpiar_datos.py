import pandas as pd

# Cargar el dataset
csv_file = "extracted_data/loan.csv"
df = pd.read_csv(csv_file, low_memory=False)

# Seleccionar las columnas clave para el análisis
columns_to_keep = [
    "loan_amnt",
    "funded_amnt",
    "funded_amnt_inv",
    "int_rate",
    "installment",
    "grade",
    "sub_grade",
    "debt_settlement_flag",
]

df_filtered = df[columns_to_keep]

# Eliminar filas con valores nulos en estas columnas clave
df_filtered = df_filtered.dropna()

# Guardar el nuevo dataset limpio
df_filtered.to_csv("cleaned_loan_data.csv", index=False)

# Mostrar informacion despues de limpiar
print(df_filtered.info())
print(df_filtered.head())
