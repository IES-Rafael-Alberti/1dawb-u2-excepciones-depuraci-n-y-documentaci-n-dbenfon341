# Intento de algoritmo burbuja.


# Definimos la funcion "burbuja" con un parametro (lista).
def algoritmoBurbuja(lista):
    # Creamos una variable llamada "num", que almacena la longitud de "lista".
    num = len(lista)
    # Creo dos bucles for como explica el ejercicio, uno haciendo de padre y otro de hijo (anidados).
    # El primer bucle (padre) recorre la lista desde el principio hasta la penúltima posición.
    for i in range(num-1):
         # Hijo, dentro del bucle "padre", compara y cambia para mover el elemento más grande al final.
         # En cada vuelta del bucle "padre", el elemento más grande se mueve a la posición correcta.
        for j in range(num-1-i):
            # Compara dos elementos adyacentes y los intercambia si están en el orden incorrecto.
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def main():
    # Se crea una lista vacía en una variable llamada "a".
    a = []
    # Creamos la variable "n", con un valor númerico que introduzca el usuario.
    n = int(input("Introduce una cantidad de números: "))
    # Hacemos un bucle for que dará vueltas tantas veces como el número introducido por el usuario para la variable "n" del punto anterior.
    for _ in range(0, n):
        # Creamos la variable "elementos", con el input del usuario, que se irá añadiendo
        # en cada iteración a la variable "a" (a la lista). Dará tantas vueltas como
        # el valor de la variable "n".
        elementos = int(input("Introduce el número que quieras añadir a la lista: "))
        a.append(elementos)

    # Creamos la variable "ListaOrdenadaBurbuja" para llamar a la función "algoritmoBurbuja", que
    # ordena la lista.
    ListaOrdenadaBurbuja = algoritmoBurbuja(a)
    print(ListaOrdenadaBurbuja)


if __name__ == "__main__":
    main()