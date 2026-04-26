import unittest
from script import Rezultatas

class TestSnake(unittest.TestCase):
    def test_tasku_pridejimas(self):
        rez = Rezultatas()
        rez.prideti_taska()
        self.assertEqual(rez.score, 1)

    def test_rekordo_resetas(self):
        rez = Rezultatas()
        rez.score = 10
        rez.rodyti_mirti()
        self.assertEqual(rez.score, 0)

if __name__ == "__main__":
    unittest.main()
