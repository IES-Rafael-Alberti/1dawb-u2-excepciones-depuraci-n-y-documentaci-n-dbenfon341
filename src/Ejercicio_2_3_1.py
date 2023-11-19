# Ejercicio 2.3.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def introducir_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad > 0:
                return edad
            else:
                print("Tu edad no puede ser un número negativo ni cero. Inténtalo de nuevo.")
        except ValueError:
            print("Debes introducir un número entero. Inténtalo de nuevo.")


def bucle_edad(edad):
    mensaje = ""
    año = 1
    while año <= edad:
        mensaje = mensaje + str(año) + " "
        año = año + 1
    return mensaje.rstrip(" ")


def main():
    edad = introducir_edad()
    final = bucle_edad(edad)
    print(final)


if __name__ == "__main__":
    main()