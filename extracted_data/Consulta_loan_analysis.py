import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a la base de datos con "with" para cerrar automáticamente
with sqlite3.connect("loans.db") as conn:
    cursor = conn.cursor()

    # Total de préstamos y monto total de préstamos
    query = """
    SELECT 
        COUNT(*) AS total_loans, 
        SUM(loan_amnt) AS total_loan_amount
    FROM loans;
    """
    cursor.execute(query)
    result = cursor.fetchall()

    total_loans = result[0][0]
    total_loan_amount = result[0][1]

    print(f"Total de préstamos: {total_loans}")
    print(f"Monto total de préstamos otorgados: ${total_loan_amount:,.2f}\n")

    # Guardar en Excel
    df_loans = pd.DataFrame(
        [[total_loans, total_loan_amount]], columns=["Total Loans", "Total Loan Amount"]
    )
    df_loans.to_excel("loan_summary.xlsx", index=False)

    # Distribución de los montos de préstamos
    df = pd.read_sql("SELECT loan_amnt FROM loans;", conn)
    plt.figure(figsize=(10, 5))
    sns.histplot(df["loan_amnt"], bins=30, kde=True)
    plt.title("Distribución de los montos de préstamos")
    plt.xlabel("Monto del préstamo")
    plt.ylabel("Frecuencia")
    plt.savefig("loan_distribution.png")  # Guardar imagen
    plt.close()

    # Tasas de interés promedio por calificación crediticia
    df = pd.read_sql(
        "SELECT grade, AVG(int_rate) AS avg_interest FROM loans GROUP BY grade;", conn
    )
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="grade",
        y="avg_interest",
        hue="grade",
        palette="coolwarm",
        legend=False,
    )
    plt.title("Tasa de interés promedio por calificación crediticia")
    plt.xlabel("Calificación (Grade)")
    plt.ylabel("Tasa de interés promedio (%)")
    plt.savefig("interest_rate_by_grade.png")  # Guardar imagen
    plt.close()

    # Guardar en Excel los datos de tasas de interés
    df.to_excel("interest_rates.xlsx", index=False)

    # Porcentaje de préstamos en proceso de liquidación
    query = """
    SELECT 
        COUNT(CASE WHEN debt_settlement_flag = 'Y' THEN 1 END) AS liquidated_loans,
        COUNT(*) AS total_loans
    FROM loans;
    """
    cursor.execute(query)
    result = cursor.fetchall()

    liquidated_loans = result[0][0]
    total_loans = result[0][1]
    percentage = (liquidated_loans / total_loans) * 100

    print(f"Total de préstamos en liquidación: {liquidated_loans}")
    print(f"Porcentaje de préstamos en liquidación: {percentage:.2f}%\n")

    # Guardar en Excel
    df_liquidation = pd.DataFrame(
        [[liquidated_loans, percentage]], columns=["Liquidated Loans", "Percentage"]
    )
    df_liquidation.to_excel("loan_liquidation.xlsx", index=False)

print("✅ Datos y gráficas guardados exitosamente.")
