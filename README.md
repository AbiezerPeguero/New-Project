# Proyecto de Análisis de Datos - New Project

## Estructura de archivos
```
New_project/
│
├── extracted_data/
│   ├── Cargar_datos_csv_pandas.py
│   ├── cleaned_loan_data.csv
│   ├── Codigo_filtrar_y_limpiar_datos.py
│   ├── Consulta_loan_analysis.py
│   ├── Crear_tabla_loans.py
│   ├── Extraer_info_zip.py
│   ├── informe_en_pdf/
│   │   ├── interest_rates.xlsx
│   │   ├── interest_rate_by_grade.png
│   │   ├── loan_distribution.png
│   │   ├── loan_liquidation.xlsx
│   │   └── loan_summary.xlsx
│   ├── LCDataDictionary.xlsx
│   ├── loan.csv
│   └── Reporte_en_pdf.py
│
├── loans.db
├── loan_analysis_report.pdf
├── .gitignore
└── requirements.txt
```

## Librerías Utilizadas
- pandas
- numpy
- matplotlib
- seaborn
- fpdf

## Instrucciones de Ejecución
1. Cargar los datos desde `loan.csv`.
2. Limpiar y filtrar los datos con `Codigo_filtrar_y_limpiar_datos.py`.
3. Realizar consultas de análisis con `Consulta_loan_analysis.py`.
4. Generar reportes en PDF con `Reporte_en_pdf.py`.

## Resultados
- Visualización de datos con gráficos generados en matplotlib y seaborn.
- Archivos Excel con datos procesados.
- Informes PDF generados con fpdf.
- Base de datos SQLite loans.db con la data procesada.

## Autor
[Abiezer Peguero]

