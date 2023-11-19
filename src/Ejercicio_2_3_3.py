# Ejercicio 2.3.3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.


def introducir_numero():
    while True:
        try:
            numero = int(input("Escribe un número: "))
            if numero > 0:
                return numero
            else:
                print("El número no puede ser negativo ni cero. Inténtalo de nuevo.")
        except ValueError:
            print("Debes introducir un número entero. Inténtalo de nuevo.")


def bucle_numero(num1):
    mensaje = ""
    cont = num1
    while cont >= 0:
        mensaje = mensaje + str(cont) + ", "
        cont = cont - 1
    return mensaje.rstrip(", ")


def main():
    numero = introducir_numero()
    final = bucle_numero(numero)
    print(final)


if __name__ == "__main__":
    main()