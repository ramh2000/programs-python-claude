import shutil
import os

# 1. Definimos el nombre del archivo original y su copia
archivo_original = "notas.txt"
archivo_respaldo = "notas_copia.txt"

# 2. Creamos un archivo de texto de prueba automáticamente
with open(archivo_original, "w", encoding="utf-8") as f:
    f.write("¡Hola! Este es el contenido de mi archivo original.")

print(f" Archivo '{archivo_original}' creado con éxito.")

# 3. Automatizamos la copia del archivo
if os.path.exists(archivo_original):
    shutil.copy(archivo_original, archivo_respaldo)
    print(f"🤖 ¡Automatización exitosa! Se creó '{archivo_respaldo}'.")
else:
    print("❌ Error: El archivo original no existe.")