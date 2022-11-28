"""
Sandra Nitchi, 2022
exercise 2
ce code créé une classe avec la longeur et largeur d'une rectangle, et calcul son aire
"""


class Rectangle:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def calcul_aire(self):
        aire = self.longeur * self.largeur
        return aire

    def afficher_infos(self):
        print(f"la rectangle a un aire de {self.calcul_aire()}, un longeur de {self.longeur} et une largeur de "
              f"{self.largeur}")


rectangle = Rectangle(2, 4)
rectangle.afficher_infos()
