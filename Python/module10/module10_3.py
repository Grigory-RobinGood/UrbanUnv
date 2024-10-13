import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 500  # Начальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайное пополнение
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайное снятие
            print(f"Запрос на снятие {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён: недостаточно средств для снятия {amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Имитация задержки


# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
