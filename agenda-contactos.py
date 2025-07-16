separador = "-" * 50

def mostrar_menu():
    print("-" * 50)
    print("Agenda de contactos:")
    print("\n1. Agregar nuevo contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Lista de contactos")
    print("5. Salir de tus contactos \n")

def buscar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    print("-" * 50)
    if nombre in agenda:
        print(separador)
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]}")
        print(f"Email: {agenda[nombre]["email"]}")
        print(separador)
    else:
        print(separador)
        print(f"No se encontro a {nombre} entre tus contactos")
        print(separador)


def agregar_contacto(agenda):
    nombre = input("Porfavor introduzca el nombre del contacto: ")
    print(separador)
    telefono = input("Por favor introduce el numero de telefono: ")
    print(separador)
    email = input("Por favor introduce el email del contacto: ")
    print(separador)
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(separador)
    print(f"Se ha agregado el contacto {nombre} exitosamente!")
    print(separador)


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desee eliminar: ")
    print(separador)
    if nombre in agenda:
        del agenda[nombre]
        print(separador)
        print(f"Se ha elminado a {nombre} de tus contactos")
        print(separador)
    else:
        print(separador)
        print(f"No se encontro a {nombre} entre tus contactos")
        print(separador)

def lista_de_contactos(agenda):
    if agenda:
        print("-" * 50)
        print("Lista de contactos: \n")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print(separador)
    else:
        print(separador)
        print("No tienes ningun contacto agregado.")
        print(separador)




def agenda_contactos():
    agenda ={}

    while True:
        
        mostrar_menu()
        opciones = input("Por favor elije una opcion: ")
        print(separador)

        if opciones == "1":
            agregar_contacto(agenda)
        elif opciones == "2":
            buscar_contacto(agenda)
        elif opciones == "3":
            eliminar_contacto(agenda)
        elif opciones == "4":
            lista_de_contactos(agenda)
        elif opciones == "5":
            print("Saliendo de la agenda de contactos")
            break
        else:
            print("Por favor selecciona una opcion existente.")

agenda_contactos()