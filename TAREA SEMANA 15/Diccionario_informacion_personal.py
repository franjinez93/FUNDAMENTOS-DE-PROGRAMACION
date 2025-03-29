# Diccionario
informacion_personal = {"nombre": "Francisco","edad": 31,"ciudad": "Quito","profesion": "Militar"}
print("Diccionario original:", informacion_personal)
#acceder a la clave ciudad
print("Accediendo a la clave ciudad:")
print(informacion_personal["ciudad"])
#modificar ciudad
informacion_personal["ciudad"]= "Ibarra"
print("Modificando la ciudad por Ibarra:")
print(informacion_personal)
#modificar profesion
informacion_personal["profesion"]= "Doctor"
print("Modificando la profesion por Doctor:")
print(informacion_personal)
#agregar el numero de telefono
if "telefono" in informacion_personal:
    print("si esta telefono")
else:
    informacion_personal["telefono"]= 2698379
    print("Se agrego Telefono:")
    print(informacion_personal)
#eliminar
del informacion_personal["edad"]
print("Se elimino la edad:")
print(informacion_personal)

#impresion de diccionario resultante
print("El diccionario resultante es:")
print(informacion_personal)