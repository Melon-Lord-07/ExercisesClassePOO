"""
Sandra Nitchi, 2022
exercise 6
ce code cree un classe hero presque identique a celle de l'exercise 4 sauf que celle la inclut l'intelligence
"""
import random


class Hero:
    def __init__(self, nom_hero):
        self.nom_hero = nom_hero
        self.points_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.intelligence = random.randint(1, 20)

    def action_attaque(self):
        return self.force_attaque + random.randint(1, 6)

    def recevoir_dommage(self, dommage):
        self.points_vie -= dommage - self.force_defense

    def est_vivant(self):
        return self.points_vie > 0

    def afficher_tout(self):
        print(f"\nNom: {self.nom_hero}"
              f"\nHP: {self.points_vie}"
              f"\nForce attaque: {self.force_attaque}"
              f"\nForce défense: {self.force_defense}"
              f"\nIntelligence: {self.intelligence}")


hero = Hero("Jeffrey the 3rd")
hero.afficher_tout()
