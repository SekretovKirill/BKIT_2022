import unittest
from fibbonachi import fibb
from collections.abc import Generator


class Test(unittest.TestCase):
    def test_sequence(self):
        fi = fibb()
        a = [next(fi) for i in range(10)]
        self.assertEqual(len(a), 10)
        self.assertListEqual(a, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

        exp = [89, 144, 233, 377, 610]
        for count, val in enumerate(fi):
            if count > 4:
                break
            self.assertEqual(val, exp[count])

    def test_generator(self):
        a = fibb()
        self.assertIsInstance(a, Generator)
        self.assertEqual(next(a), 1)
        self.assertEqual(next(a), 1)
        self.assertEqual(next(a), 2)
        self.assertEqual(next(a), 3)
        

    def test_func(self):
        fi = fibb()
        a = list(zip(range(5), fi))
        self.assertEqual(len(a), 5)
        self.assertListEqual(a, [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5)])

        a = list(zip(range(5), fi))
        self.assertEqual(len(a), 5)
        self.assertListEqual(a, [(0, 8), (1, 13), (2, 21), (3, 34), (4, 55)])


if __name__ == "__main__":
    unittest.main()
