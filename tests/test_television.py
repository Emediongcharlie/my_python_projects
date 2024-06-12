import unittest

from television import television


class MyTestCase(unittest.TestCase):
    def test_television_is_on(self):
        my_television = television()
        self.assertEqual(my_television.is_on(), True)  # add assertion here

    def test_television_is_off(self):
        my_television = television()
        self.assertEqual(my_television.is_off(), False)

    def test_television_is_on_and_can_increase_volume(self):
        my_television = television()
        self.assertEqual(my_television.can_increase_volume(26), 27)

    def test_television_is_on_and_can_decrease_volume(self):
        my_television = television()
        self.assertEqual(my_television.can_decrease_volume(24), 23)

    def test_television_can_increase_channel(self):
        my_television = television()
        self.assertEqual(my_television.increase_channel(10), 11)

    def test_television_can_decrease_volume(self):
        my_television = television()
        self.assertEqual(my_television.decrease_channel(15), 14)

if __name__ == '__main__':
    unittest.main()
