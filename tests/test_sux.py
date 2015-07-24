import unittest
import some

class MikeTest(unittest.TestCase):
    def test_choices(self):
        self.assertEqual(10, len(some.my_list))
