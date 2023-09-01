# Almacena los números

lista = []


def menu():
    print("A) Agregar un número a la lista:")
    print("B) Agregar un número a la lista según la posición:")
    print("C) Ver longitud de la lista")
    print("D) Eliminar el último número")
    print("E) Eliminar un número")
    print("F) Contar repeticiones de un número")
    print("G) Salir")

    # Ejecuta una opcion del menu


def seleccionarOpcion(opcion):
    if opcion.upper() == "A":
        numero = int(input("\nIngresa un número: "))
        lista.append(numero)
    elif opcion == "B":
        posicion = int(input("\nIngresa la posición: "))
        numero = int(input("\nIngresa un número: "))
        lista.insert(posicion, numero)
    elif opcion == "C":
        print("La longitud de la lista es de {0}".format(len(lista)))
    elif opcion == "D":
        numero = lista.pop()
        print("Se borro el numero {0}".format(numero))
    elif opcion == "E":
        print("De la lista, que número desea borrar? ", lista)
        numero = int(input("Ingresa el numero a borrar: "))
        lista.remove(numero)
        print("Se borro {0}".format(numero))
    elif opcion == "F":
        numero = int(input("Ingresa el número que desea contar: "))
        total = lista.count(numero)
        print("En la lista {0} se repite {1}".format(numero, total))
    elif opcion == "G":
        print("Gracias por usar nuestro programa :)")
    else:
        print("Esta opcion no es valida!!!")


while True:
    menu()

    opcion = input("Ingresa una opcion A-G: ")
    seleccionarOpcion(opcion)

    print("Lista de datos", lista)

    if opcion.upper() == "G":
        break
