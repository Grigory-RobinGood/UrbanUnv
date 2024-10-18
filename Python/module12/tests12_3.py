import unittest
from module12_2 import TournamentTest, Runner, Tournament
from module12_1 import RunnerTest, Runner


class Runnertest(RunnerTest):
    is_frozen = True

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("test runner")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("test runner")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("runner first")
        runner2 = Runner("runner second")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class Tournamenttest(TournamentTest):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усейн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in cls.all_results.items():
            print(f'Бегун {runner.name}:{place} место')

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_tournament_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)].name == 'Ник')

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_tournament_andrei_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)].name == 'Ник')

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_tournament_usain_andrei_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
