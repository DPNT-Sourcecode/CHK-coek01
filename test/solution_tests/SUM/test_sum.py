from unittest import TestCase

from lib.solutions.SUM import sum_solution


class TestSum(TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_zero(self):
        assert sum_solution.compute(0, 0) == 0

    def test_sum_none(self):
        with self.assertRaises(Exception):
            sum_solution.compute(None, None)
