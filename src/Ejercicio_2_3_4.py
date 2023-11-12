# Ejercicio 2.3.4
# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.


def pedirNumero(num1):
    try:
        num1 = int(num1)
        return num1
    except ValueError:
        print("La entrada no es correcta.")
        raise


def main():
        numero = input("Introduce un número entero: ")
        final = pedirNumero(numero)
        print(final)


if __name__ == "__main__":
    main()