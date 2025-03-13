import zipfile
import os

# Nombre del archivo zip
zip_file = "archive (1).zip"

# Crear carpeta para extraer los datos
extract_folder = "extracted_data"
os.makedirs(extract_folder, exist_ok=True)

# Extraer los archivos
with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall(extract_folder)

# Listar los archivos extraidos
extracted_files = os.listdir(extract_folder)
print("Archivos extraidos:")
for file in extracted_files:
    print(file)
