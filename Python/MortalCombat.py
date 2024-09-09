class Hero:
    def __init__(self, health=100, level=1, attack_damage=10):
        self.health = health
        self.level = level
        self.attack_damage = attack_damage
        self.inventory = Inventory()
        self.experience = 0  # Опыт для повышения уровня

    def find_item(self, item):
        self.inventory.add_item(item)
        print(f"Вы нашли {item.name}!")

    def attack(self, mob):
        mob.health -= self.attack_damage
        print(
            f"Вы напали на {mob.name} и нанесли {self.attack_damage} урона. У {mob.name} осталось {mob.health} здоровья.")

    def use_item(self, item_name):
        item = self.inventory.get_item(item_name)
        if item:
            item.use(self)
            self.inventory.remove_item(item_name)
        else:
            print(f"У вас нет {item_name} в инвентаре.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"Вы получили {amount} опыта.")
        if self.experience >= 100:  # Условие для повышения уровня
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20  # Увеличение здоровья при повышении уровня
        self.attack_damage += 5  # Увеличение урона при повышении уровня
        self.experience = 0  # Сброс опыта
        print(f"Поздравляем! Вы достигли уровня {self.level}!")

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

    def remove_item(self, item_name):
        item = self.get_item(item_name)
        if item:
            self.items.remove(item)
            return True
        return False

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def show_items(self):
        return ', '.join(item.name for item in self.items) if self.items else 'пусто'


class Item:
    def __init__(self, name, effect_type, effect_value):
        self.name = name  # Название предмета
        self.effect_type = effect_type  # Тип эффекта: 'heal' или 'boost'
        self.effect_value = effect_value  # Значение эффекта

    def use(self, hero):
        if self.effect_type == 'heal':
            hero.health += self.effect_value
            print(f"Вы использовали {self.name}, восстановив {self.effect_value} здоровья!")
        elif self.effect_type == 'boost':
            hero.attack_damage += self.effect_value
            print(f"Вы использовали {self.name}, увеличив урон атаки на {self.effect_value}!")


def main():
    hero = Hero()
    orc = Mob("Орк", 50, 15)

    # Создаем предметы
    healing_potion = Item("Зелье здоровья", "heal", 20)
    attack_boost = Item("Эликсир силы", "boost", 5)

    hero.find_item(healing_potion)
    hero.find_item(attack_boost)
    hero.show_status()

    print("\nНачинается бой!")
    while hero.health > 0 and orc.health > 0:
        action = input(
            "Выберите действие (атака (введите 1) / "
            "использование зелья 'Зелье здоровья' (введите 2) / "
            "использование 'Эликсир силы' (введите 3)): ").strip().lower()

        if action == "1":
            hero.attack(orc)
        elif action == "2":
            hero.use_item("Зелье здоровья")
        elif action == "3":
            hero.use_item("Эликсир силы")
        else:
            print("Недопустимое действие. Попробуйте снова.")
            continue  # Пропускаем итерацию цикла

        if orc.health > 0:
            orc.attack(hero)
        print()

    if hero.health > 0:
        print(f"Вы победили {orc.name}!")
        hero.gain_experience(50)  # Получаем опыт за победу
    else:
        print(f"Вы были побеждены {orc.name}...")


if __name__ == '__main__':
    main()
