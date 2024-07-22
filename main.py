from abc import ABC, abstractmethod
import random


class Character(ABC):
    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def is_alive(self):
        pass


class Hero(Character):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        decrement = int(self.attack_power * random.uniform(0.5, 1.5))
        other.health -= decrement
        print(f'{self.name} атакует {other.name}, {other.name} потерял {decrement} здоровья')

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break
        else:
            print("Ничья!")


player = Hero("Герой", 100, 20)
computer = Hero("Компьютер", 100, 20)
game = Game(player, computer)
game.start()
