import random


tab = [random.randint(1, 100) for i in range(15)]
print("Tableau avant le tri :", tab)

def ordre_croissant(tableau):
    for i in range(1, len(tableau)):
        croissante = tableau[i]
        j = i - 1 

        while j >= 0 and tableau[j] > croissante:
            tableau[j + 1] = tableau[j]
            j -= 1

        tableau[j + 1] = croissante


ordre_croissant(tab)
print("Tableau après le tri :", tab)
