from unittest import TestCase


from lib.solutions.CHK import checkout_solution


class TestHello(TestCase):
    def test_all_items(self):
        self.assertEquals(115, checkout_solution.checkout("ABCD"))