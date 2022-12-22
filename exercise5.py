"""
Sandra Nitchi, 2022
exercise 5
Ce code créé une dataclass avec les caracteristiques d'un personage de D&D
"""
import random
from dataclasses import dataclass


@dataclass
class Stats:
    force: int = random.randint(1, 20)
    dexterity: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class Test:
    def __init__(self):
        self.stats = Stats()


test = Test()
print(test.stats)
