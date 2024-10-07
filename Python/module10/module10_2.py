import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {'день' if self.days == 1 else 'дня'}!")


# Создание и запуск потоков
knight1 = Knight("Рыцарь Артур", 30)
knight2 = Knight("Рыцарь Ланселот", 40)

knight1.start()
knight2.start()

# Ожидание завершения обоих потоков
knight1.join()
knight2.join()

print("Битвы окончены.")