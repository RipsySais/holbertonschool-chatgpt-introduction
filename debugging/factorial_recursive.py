#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle de n de manière récursive.

    Arguments :
    n (int) : Le nombre dont on veut calculer la factorielle.

    Retourne :
    int : La factorielle de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        try:

            f = factorial(int(sys.argv[1]))
            print(f)
        except ValueError:

            print("Veuillez fournir un argument entier valide.")
    else:
        print("Veuillez fournir un argument.")
