# Definir tupla con meses del año
meses = (
    "enero", "febrero", "marzo", "abril",
    "mayo", "junio", "julio", "agosto",
    "septiembre", "octubre", "noviembre", "diciembre"
)

# Solicitar al usuario un número entre 1 y 12
try:
    numero_mes = int(input("Ingresa un número entre 1 y 12: "))

    if 1 <= numero_mes <= 12:
        mes_correspondiente = meses[numero_mes - 1]
        print(
            f"Mes: {numero_mes} es {mes_correspondiente}.")
    else:
        print("Error: El número debe estar entre 1 y 12.")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")
