# Solicitar al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Convertir la cadena a una lista de palabras
lista_palabras = cadena.split()

# Calcular la cantidad de palabras en la lista
cantidad_palabras = len(lista_palabras)

# Mostrar el resultado
print(f"La cadena tiene {cantidad_palabras} palabra(s).")
