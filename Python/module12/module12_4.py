import logging
import unittest

logging.basicConfig(
    level=logging.INFO, filemode='w', encoding="utf-8", filename='runner_tests.log',
    format="%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = True

    def test_walk(self):
        try:
            runner = Runner("test runner", -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f"'test_walk' выполнен успешно")
        except ValueError:
            logging.warning(f"Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(True)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning(f"Не верный тип данных")

    def test_challenge(self):
        runner1 = Runner("runner first")
        runner2 = Runner("runner second")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
