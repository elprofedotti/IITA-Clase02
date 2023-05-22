from funciones import solicitar_numeros, mostrar_menu, realizar_operacion, cantidad_numeros
def main():
    while True:
        mostrar_menu()
        operacion = int(input("Elige una operación: "))
        if operacion == 7:
            print("Terminando calculadora...")
            break
        if operacion in [5, 6]:
            cantidad=2
        else:
            cantidad=cantidad_numeros()
        
        numeros = solicitar_numeros(cantidad)
        resultado = realizar_operacion(operacion, numeros)
        if resultado is not None:
            print(f"El resultado de la operación es: {resultado}\n")
        respuesta = input("¿Quieres hacer otra operación? (si/no): ").lower()
        if respuesta != 'si':
            print("Terminando la calculadora...")
            break

if __name__ == "__main__":
    main()
