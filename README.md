# Lista para almacenar los textos del programa
mensaje = [
    "¡Bienvenido al Directorio Telefónico!",
    "Ingrese el Nombre y Apellido: ",
    "Ingrese el Teléfono: ",
    "Ingrese el Correo Electrónico: ",
    "Ingrese la Fecha de Cumpleaños (dia/mes): ",
   
    "Menú Principal:\n1. Busca por teléfono celular\n2. Agregar un nuevo registro\n3. Borrar un registro\n4. Salir de la aplicación\nSeleccione una opción: ",
    "Ingrese el número de teléfono para buscar: ",
    "Ingrese el número de teléfono para borrar: ",
    "agregado exitosamente.",
    " no encontrado.",
    "eliminado exitosamente.",
    "afuera del proceso"
]

# Lista para almacenar la información de las personas
directorio = []

# Diccionario único que se sobrescribe para cada registro
registro = {}

def limpiar_pantalla():
    print("\n" * 100)  # Simula la limpieza de la pantalla

def agregar_registro():
    registro.clear()  # Limpiar el diccionario antes de usarlo
    registro["Nombre y Apellido"] = input(mensaje[1])
    registro["Teléfono"] = int(input(mensaje[2]))
    registro["Correo"] = input(mensaje[3])
    registro["Cumpleaños"] = input(mensaje[4])
    directorio.append(registro.copy())  # Guardar una copia del diccionario
    print(mensaje[8])

def buscar_por_telefono():
    telefono = int(input(mensaje[6]))
    encontrado = False
    for persona in directorio:
        if persona["Teléfono"] == telefono:
            limpiar_pantalla()  # Limpiar la pantalla antes de mostrar la información
            print("Información encontrada:")
            print(f"Nombre y Apellido: {persona['Nombre y Apellido']}")
            print(f"Teléfono: {persona['Teléfono']}")
            print(f"Correo: {persona['Correo']}")
            print(f"Cumpleaños: {persona['Cumpleaños']}")
            encontrado = True
            break
    if not encontrado:
        print(mensaje[9])

def borrar_registro():
    telefono = int(input(mensaje[7]))
    for persona in directorio:
        if persona["Teléfono"] == telefono:
            directorio.remove(persona)
            print(mensaje[10])
            return
    print(mensaje[9])

# Programa principal
print(mensaje[0])

while True:
    opcion = input(mensaje[5])
    if opcion == "1":
        buscar_por_telefono()
    elif opcion == "2":
        agregar_registro()        
    elif opcion == "3":
        borrar_registro()
    elif opcion == "4":
        print(mensaje[11])
        break
    else:
        print("Opción no válida, intente de nuevo.")
