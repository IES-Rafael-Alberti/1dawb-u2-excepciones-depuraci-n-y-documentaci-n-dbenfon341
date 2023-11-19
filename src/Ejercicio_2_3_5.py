# Ejercicio 2.3.5
# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"


def verificar_pwd(pwd_ingresada):
    pwd_correcta = "meloinvento1122"
    if pwd_ingresada == pwd_correcta:
        return "Contraseña correcta!!"
    else:
        raise NameError("Incorrect Password!!")


def main():
        pwd_ingresada = input("Ingresa la contraseña: ")
        final = verificar_pwd(pwd_ingresada)
        print (final)


if __name__ == "__main__":
    main()