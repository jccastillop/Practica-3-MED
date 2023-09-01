# Leer las 5 notas del alumno y almacenarlas en una lista
notas = []
for i in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

# Mostrar todas las notas
print("Notas obtenidas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

# Calcular la nota media
nota_media = sum(notas) / len(notas)
print(f"Nota media: {nota_media:.2f}")

# Encontrar la nota más alta y la nota más baja
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
