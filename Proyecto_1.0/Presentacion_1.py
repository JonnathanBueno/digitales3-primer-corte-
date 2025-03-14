# proyecto de digitales3
# Lista para almacenar los textos del programa
mensaje = [
    "¡Bienvenido al Directorio Telefónico!",
    "Ingrese el Nombre y Apellido: ",
    "Ingrese el Teléfono Celular: ",
    "Ingrese la Fecha de Cumpleaños (DD/MM): ",
    "Ingrese el Correo Electrónico: ",
    "Menú Principal:\n1. Agregar un nuevo registro\n2. Buscar una persona por teléfono celular\n3. Borrar un registro\n4. Salir de la aplicación\nSeleccione una opción: ",
    "Ingrese el número de teléfono celular para buscar: ",
    "Ingrese el número de teléfono celular para borrar: ",
    "Registro agregado exitosamente.",
    "Registro no encontrado.",
    "Registro eliminado exitosamente.",
    "Saliendo de la aplicación. ¡Hasta pronto!"
]

# Lista para almacenar la información de las personas
directorio = []

# Diccionario único que se sobrescribe para cada registro
registro = {}

def agregar_registro():
    registro.clear()  # Limpiar el diccionario antes de usarlo
    registro["Nombre y Apellido"] = input(mensaje[1])
    registro["Teléfono Celular"] = int(input(mensaje[2]))
    registro["Cumpleaños"] = input(mensaje[3])
    registro["Correo"] = input(mensaje[4])
    directorio.append(registro.copy())  # Guardar una copia del diccionario
    print(mensaje[8])

def buscar_por_telefono():
    telefono = int(input(mensaje[6]))
    encontrado = False
    for persona in directorio:
        if persona["Teléfono Celular"] == telefono:
            print("Información encontrada:")
            print(f"Nombre y Apellido: {persona['Nombre y Apellido']}")
            print(f"Teléfono Celular: {persona['Teléfono Celular']}")
            print(f"Cumpleaños: {persona['Cumpleaños']}")
            print(f"Correo: {persona['Correo']}")
            encontrado = True
            break
    if not encontrado:
        print(mensaje[9])


def borrar_registro():
    telefono = int(input(mensaje[7]))
    for persona in directorio:
        if persona["Teléfono Celular"] == telefono:
            directorio.remove(persona)
            print(mensaje[10])
            return
    print(mensaje[9])

# Programa principal
print(mensaje[0])

while True:
    opcion = input(mensaje[5])
    if opcion == "1":
        agregar_registro()
    elif opcion == "2":
        buscar_por_telefono()
    elif opcion == "3":
        borrar_registro()
    elif opcion == "4":
        print(mensaje[11])
        break
    else:
        print("Opción no válida. Intente de nuevo.")
