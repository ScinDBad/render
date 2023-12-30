import math

def is_prime(n):

    """
    Determina si el número es primo o no
    Parameters:
    - n (int): Número de entero a evaluar.

    Returns:
    - Bool: Verdadero si el número es primo.
    
    """

    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True

def main():

    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
