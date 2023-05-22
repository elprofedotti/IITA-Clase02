from funciones import solicitar_numeros, mostrar_menu, realizar_operacion
def main():
    while True:
        while True:
            try:
                cantidad = int(input("¿Cuántos números quieres operar? "))
                break
            except ValueError:
                print("Por favor ingresa un número válido.")
        numeros = solicitar_numeros(cantidad)
        mostrar_menu()
        operacion = int(input("Elige una operación: "))
        resultado = realizar_operacion(operacion, numeros)
        if resultado is not None:
            print(f"El resultado de la operación es: {resultado}\n")
        
        respuesta = input("¿Quieres hacer otra operación? (si/no): ").lower()
        if respuesta != 'si':
            print("Terminando la calculadora...")
            break

if __name__ == "__main__":
    main()
