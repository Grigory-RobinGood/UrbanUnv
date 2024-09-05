class Hero:


    def __init__(self, health=100, level=1, attack_damage=10, item_self=0, item_attack=0):
        self.health = health * level + item_self
        self.level = level
        self.attack_damage = attack_damage + item_attack
        self.inventory = Inventory()
        self.item_self = item_self
        self.item_attack = item_attack

    def find_item(self, item_self, item_attack):
        self.inventory.add_item(item_self)
        self.inventory.add_item(item_attack)
        print(f"Вы нашли {item_self} и {item_attack}")

    def attack(self, mob):
        mob.health -= self.attack_damage
        print(
            f"Вы напали на {mob.name} и нанесли {self.attack_damage} урона. У {mob.name} осталось {mob.health} здоровья.")

    def use_item(self, item_name):
        if self.inventory.remove_item(item_name):
            print(f"Вы использовали {item_name}.")
            if item_name == 'потерянный меч':
                self.attack_damage += 5
                print(f"Ваш урон атаки увеличен на 5!")
            else:
                print(f"У вас нет {item_name} в инвентаре")

    def show_status(self):
        health_status = f"Здоровье героя: {self.health}"
        inventory_status = f"Инвентарь героя: {self.inventory.show_items()}"
        level_status = f"Уровень героя: {self.level}"
        attack_status = f"Урон атаки героя: {self.attack_damage}"
        print(health_status)
        print(inventory_status)
        print(level_status)
        print(attack_status)


class Mob:

    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, hero):
        hero.health -= self.attack_damage
        print(f"{self.name} напал на вас и нанес {self.attack_damage} урона. У вас осталось {hero.health} здоровья.")


class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def show_items(self):
        return ', '.join(self.items) if self.items else 'пусто'


def main():
    hero = Hero()
    orc = Mob("Орк", 50, 15)
    hero.find_item('меч', 'щит')
    hero.show_status()

    print("\nНачинается бой!")
    while hero.health > 0 and orc.health > 0:
        hero.attack(orc)
        if orc.health > 0:
            orc.attack(hero)
        print()

    if hero.health > 0:
        print(f"Вы победили {orc.name}!")
    else:
        print(f"Вы были побеждены {orc.name}...")


if __name__ == '__main__':
    main()
