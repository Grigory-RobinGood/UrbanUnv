import unittest
from module12_2 import TournamentTest
from module12_1 import RunnerTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner()

