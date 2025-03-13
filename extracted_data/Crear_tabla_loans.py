import sqlite3
import pandas as pd

with sqlite3.connect("loans.db") as conn:
    cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_amnt INTEGER,
    funded_amnt INTEGER,
    funded_amnt_inv REAL,
    int_rate REAL,
    installment REAL,
    grade TEXT,
    sub_grade TEXT,
    debt_settlement_flag TEXT
);
"""
)

# Cargar los datos desde el CSV limpio
df_filtered = pd.read_csv("extracted_data/cleaned_loan_data.csv")

# Insertar los datos en la tabla SQLite
df_filtered.to_sql("loans", conn, if_exists="replace", index=False)

# Verificar que los datos se insertaron correctamente
cursor.execute("SELECT COUNT(*) FROM loans")
num_rows = cursor.fetchone()[0]

conn.commit()

print(f"✅ Datos guardados en SQLite. Total de registros: {num_rows}")
