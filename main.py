from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def hit_level(self):
        pass


# Шаг 2: Конкретные классы оружия
class Sword(Weapon):
    def __init__(self):
        self.hitLevel = 10

    def attack(self):
        return "удар мечом"

    def hit_level(self):
        return self.hitLevel


class Bow(Weapon):
    def __init__(self):
        self.hitLevel = 20

    def attack(self):
        return "выстрел из лука"

    def hit_level(self):
        return self.hitLevel


class Axe(Weapon):
    def __init__(self):
        self.hitLevel = 30

    def attack(self):
        return "сильный удар топором"

    def hit_level(self):
        return self.hitLevel


class Fireball(Weapon):
    def __init__(self):
        self.hitLevel = 40

    def attack(self):
        return "удар молнией"

    def hit_level(self):
        return self.hitLevel


# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # По умолчанию оружие не выбрано

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбрал оружие: {type(weapon).__name__}.")

    def attack(self, monster):
        if self.weapon:
            attack_message = self.weapon.attack()
            print(f"{self.name} наносит {attack_message}.")
            monster.take_damage(self.weapon.hit_level())
        else:
            print(f"{self.name} не выбрал оружие!")


# Класс монстра
class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, hitLevel):
        self.health -= hitLevel
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")


# Создаём бойца и монстра
fighter = Fighter("Игрок")
monster = Monster()

# Боец атакует
fighter.attack(monster)

# Боец выбирает меч и атакует
sword = Sword()
fighter.change_weapon(sword)
fighter.attack(monster)

# Боец выбирает лук и снова атакует
bow = Bow()
fighter.change_weapon(bow)
fighter.attack(monster)

# Боец выбирает топор и снова атакует
axe = Axe()
fighter.change_weapon(axe)
fighter.attack(monster)

# Боец выбирает огненный шар и снова атакует
fireball = Fireball()
fighter.change_weapon(fireball)
fighter.attack(monster)
