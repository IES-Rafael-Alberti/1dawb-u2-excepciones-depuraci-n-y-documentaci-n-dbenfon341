# Ejercicio 2.3.2
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def bucle_numero(numero):
    mensaje = ""
    cont = 1
    while cont <= numero:
        if cont % 2 != 0:
            mensaje = mensaje + str(cont) + ", "
        cont = cont + 1
    return mensaje.rstrip(", ")


def main():
    try:
        numero = int(input("Introduce un número: "))
        if numero <= 0:
            print("Debe introducir un número positivo.")
        else:
            final = bucle_numero(numero)
            print(final)
    except ValueError:
        print("Introduce un número correcto.")


if __name__ == "__main__":
    main()