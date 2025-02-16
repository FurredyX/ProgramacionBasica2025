import os

# Definir la ruta y el nombre del archivo
path = "D:\\Github\\"  # Agregar barra invertida para que Windows interprete la ruta correctamente
name = "miarchivo"
ext = "lagr"
file_path = path + name + "." + ext

# Verificar si el archivo existe antes de leerlo
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf8") as miarchivo:
        for line in miarchivo:
            print(line.strip())  # .strip() elimina saltos de línea y espacios extra

else:
    print("El archivo no existe.")

# Datos para escribir/modificar
lista = [90, 95, 88]

# Abrir el archivo en modo "r+" para leer y modificar el contenido
with open(file_path, "a", encoding="utf8") as miarchivo:  # "a" agrega texto sin borrar lo anterior
    miarchivo.write("\n1er P\t2do P\t3er P\tProm\n")
    miarchivo.write(f"{lista[0]}\t{lista[1]}\t{lista[2]}\t{sum(lista)/len(lista)}\n")

# Crear otro archivo y escribir en él
archivito_path = path + name + "1.txt"
with open(archivito_path, "w", encoding="utf8") as archivito:
    archivito.write("Mi archivo está corrioso.\n")

print("Modificación y escritura completadas.")