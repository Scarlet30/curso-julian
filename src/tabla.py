# Pedir dos enteros positivos al usuario e imprimir la tabla de multiplicar del primer número hasta el segundo.
from .utils import get_positive_number


def get_mutiplay():
    number1 = get_positive_number()
    number2 = get_positive_number()
    for number in range(1, number2 + 1):
        print(f"{number1} x {number} = {number1 * number} ")


get_mutiplay()
