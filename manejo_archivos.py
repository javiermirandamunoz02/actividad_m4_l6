# ACTIVIDAD M4 L6: MANEJO DE ARCHIVOS EN PYTHON


# 1. ESCRIBIR EN UN ARCHIVO
print("--- 1. Escribiendo en datos.txt ---")
archivo = open("datos.txt", "w", encoding="utf-8")
archivo.write("Línea 1: Aprendiendo a persistir datos en Python.\n")
archivo.write("Línea 2: El manejo de archivos es fundamental.\n")
archivo.write("Línea 3: Practicando con el método write().\n")
archivo.close()
print("Archivo creado y escrito con éxito.\n")

# 2. LEER EL ARCHIVO COMPLETO
print("--- 2. Leyendo contenido con read() ---")
archivo = open("datos.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()

# 3. LEER LÍNEA POR LÍNEA
print("\n--- 3. Leyendo línea por línea ---")
archivo = open("datos.txt", "r", encoding="utf-8")

primera_linea = archivo.readline()
print(f"Primera línea leída: {primera_linea.strip()}")


print("Resto del archivo mediante ciclo for:")
for linea in archivo:
    print(linea.strip())
archivo.close()

# 4. AÑADIR CONTENIDO (MODO APPEND)
print("\n--- 4. Añadiendo contenido con append ('a') ---")
archivo = open("datos.txt", "a", encoding="utf-8")
archivo.write("Línea 4: Esta línea fue agregada posteriormente.\n")
archivo.close()


print("Contenido final actualizado:")
with open("datos.txt", "r", encoding="utf-8") as archivo_lectura:
    print(archivo_lectura.read())

# 5. ATRIBUTOS Y CIERRE
print("\n--- 5. Atributos del archivo ---")
archivo_final = open("datos.txt", "r", encoding="utf-8")
print(f"Nombre del archivo (.name): {archivo_final.name}")
print(f"Modo de apertura (.mode): {archivo_final.mode}")
print(f"¿Está cerrado antes de close()? {archivo_final.closed}")

archivo_final.close()
print(f"¿Está cerrado después de close()? {archivo_final.closed}")