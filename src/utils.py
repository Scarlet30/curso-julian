# Pedir un número entero positivo al usuario. Si el dato que el usuario ingresa es inválido, volver a pedirlo hasta
# que sea válido.


def get_positive_number():
    while True:
        number = (input("Ingresa un número entero positivo: "))
        #numberC = int(number)
        if number.isdigit() and int(number) > 0:
            print(f'El número es {number}. ¡El número que ingresaste es válido!')
            return int(number)
        else:
            print("Número inválido. Debes ingresar un numero entero positivo")


get_positive_number()
