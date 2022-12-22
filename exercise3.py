"""
Sandra Nitchi, 2022
exercise 3
ce code créé une classe avec la rayon d'une cercle et calcul son aire et sa circonference
"""

from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon ** 2

    def calcul_circonference(self):
        return pi * self.rayon * 2

    def afficher_infos(self):
        print(f"le cercle a un aire d'environ {self.calcul_aire()}, une circonférence d'environ "
              f"{self.calcul_circonference()} et un rayon de {self.rayon}")


cercle = Cercle(3)
cercle.afficher_infos()
