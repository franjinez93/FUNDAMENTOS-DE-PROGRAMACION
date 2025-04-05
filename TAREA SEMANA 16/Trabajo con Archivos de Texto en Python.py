# Creacion del archivo
file_name = "my_notes.txt"

# Modo de apertura: "w" para escritura (write)
archivo_datos_personales = open(file_name, "w")

# Escibimos tres lineas con datos personales
archivo_datos_personales.write("Línea 1: Francisco Jinez.\n")
archivo_datos_personales.write("Línea 2: 31 años de edad.\n")
archivo_datos_personales.write("Línea 3: Estudiante de Ingenieria en TICS\n")

#Cerramos el archivo de escritura
archivo_datos_personales.close()

# Apertura: "r" para lectura del archivo
archivo_lectura = open(file_name, "r")

#Utilizamos el metodo readline
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()

#Mostramos en pantalla el contenido del archivo linea por linea
print("\nDatos personales línea por línea usando readline():")
print(linea_1.strip())  # strip() elimina el salto de línea al final
print(linea_2.strip())
print(linea_3.strip())

# Cerramos el archivo de lectura
archivo_lectura.close()