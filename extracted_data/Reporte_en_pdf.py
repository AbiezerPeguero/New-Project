from fpdf import FPDF
import pandas as pd

# Crear un objeto PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)


# Función para agregar una página con título
def add_section(title):
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, title, ln=True, align="C")
    pdf.ln(10)


# Sección 1: Resumen de Préstamos
add_section("Resumen de Préstamos")
df_summary = pd.read_excel(
    r"C:\Users\LENOVO 11E\Desktop\New project\extracted_data\informe_en_pdf\loan_summary.xlsx"
)
pdf.set_font("Arial", size=10)
for index, row in df_summary.iterrows():
    pdf.cell(200, 6, f"Total Loans: {row['Total Loans']}", ln=True)
    pdf.cell(200, 6, f"Total Loan Amount: {row['Total Loan Amount']}", ln=True)
pdf.ln(5)

# Sección 2: Distribución de los montos de préstamos
add_section("Distribución de los Montos de Préstamos")
pdf.image(
    r"C:\Users\LENOVO 11E\Desktop\New project\extracted_data\informe_en_pdf\loan_distribution.png",
    x=10,
    w=180,
)
pdf.ln(10)

# Sección 3: Tasas de Interés por Calificación Crediticia
add_section("Tasas de Interés por Calificación Crediticia")
pdf.image(
    r"C:\Users\LENOVO 11E\Desktop\New project\extracted_data\informe_en_pdf\interest_rate_by_grade.png",
    x=10,
    w=180,
)
pdf.ln(10)
df_interest = pd.read_excel(
    r"C:\Users\LENOVO 11E\Desktop\New project\extracted_data\informe_en_pdf\interest_rates.xlsx"
)
for index, row in df_interest.iterrows():
    pdf.cell(200, 6, f"{row['grade']}: {row['avg_interest']}%", ln=True)
pdf.ln(5)

# Sección 4: Préstamos en Liquidación
add_section("Préstamos en Liquidación")
df_liquidation = pd.read_excel(
    r"C:\Users\LENOVO 11E\Desktop\New project\extracted_data\informe_en_pdf\loan_liquidation.xlsx"
)
for index, row in df_liquidation.iterrows():
    pdf.cell(200, 6, f"{row['Liquidated Loans']}: {row['Percentage']}%", ln=True)
pdf.ln(5)

# Guardar el PDF
pdf_filename = "loan_analysis_report.pdf"
pdf.output(pdf_filename)
print(f"Informe PDF guardado como: {pdf_filename}")
