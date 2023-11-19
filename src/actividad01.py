"""
Actividad 1: 
    Escribe un programa que capture la excepción división entre cero. Tendrá que mostar el mensaje del error capturado.
"""

def dividir(num1: float, num2: float = 1) -> float:
    resultado = None
    resultado = num1 / num2
    resultado = round(resultado, 2)
    return resultado


def pedirNumero(msj: str) -> float:

    numero = None

    try:
        numero = float(input(msj))
    except:
       print("**Error** Número introducido no válido")
    return numero


def main():

    dividendo = pedirNumero("Introduzca el dividendo: ")

    if dividendo != None:
        divisor = pedirNumero("Introduzca el divisor: ")
        if divisor != None:
            resultado = None
            try:
                resultado = dividir(dividendo, divisor)
            except ZeroDivisionError:
                print("**Error** No es posible realizar la división por cero.")
            except:
                print("**Error** Se produjo un error y no es posible realizar la división.")
            if resultado != None:
                print(f"El resultado es {resultado}")


if __name__ == "__main__":
    main()
