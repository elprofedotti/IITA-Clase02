def solicitar_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingresa el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor ingresa un número válido.")
    return numeros

def mostrar_menu():
    print("""
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    """)

def realizar_operacion(operacion, numeros):
    if operacion == 1:
        return sum(numeros)
    elif operacion == 2:
        return numeros[0] - sum(numeros[1:])
    elif operacion == 3:
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado
    elif operacion == 4:
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num
        return resultado
    else:
        print("Opción no válida")
        return None