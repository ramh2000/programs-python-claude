# Definimos el nombre del archivo que queremos leer
nombre_archivo = "mi_archivo.txt"

try:
    # Abrimos el archivo en modo lectura ('r') usando 'with' para cerrarlo automáticamente
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        print("--- Leyendo el archivo correctamente ---")
        # Leemos y mostramos el contenido completo
        contenido = archivo.read()
        print(contenido)
        print("---------------------------------------")
except FileNotFoundError:
    # Este bloque se ejecuta si el archivo txt no existe en la misma carpeta
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    print("Asegúrate de que el archivo TXT esté en la misma carpeta que este script.")
