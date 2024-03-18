import unittest
from Homework1 import *
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bear = Bear("Brown Bear")
        self.wolf = Wolf("Grey Wolf")
        self.rabbit = Rabbit("White Rabbit")

    def test_wolf_speak(self):
        self.assertEqual(self.wolf.speak(), "Woof")

    def test_bear_speak(self):
        self.assertEqual(self.bear.speak(), "Arrh")

    def test_rabbit_speak(self):
        self.assertEqual(self.rabbit.speak(), "Squeak")

    def test_wolf_eat(self):
        self.assertEqual(self.wolf.eat(), "Meat")

    def test_bear_eat(self):
        self.assertEqual(self.bear.eat(), "All")

    def test_rabbit_eat(self):
        self.assertEqual(self.rabbit.eat(), "Plants")


if __name__ == '__main__':
    unittest.main()
