from unittest import TestCase


from lib.solutions.CHK import checkout_solution


class TestHello(TestCase):
    def test_all_items(self):
        self.assertEquals(115, checkout_solution.checkout("ABCD"))

    def test_invalid_item(self):
        self.assertEquals(-1, checkout_solution.checkout("ABCDF"))

    def test_invalid_input(self):
        self.assertEquals(-1, checkout_solution.checkout(10))

    def test_empty_shopping_cart(self):
        self.assertEquals(0, checkout_solution.checkout(""))

    def test_promotions(self):
        self.assertEquals(130, checkout_solution.checkout("AAA"))
        self.assertEquals(260, checkout_solution.checkout("AAAAAA"))
        self.assertEquals(180, checkout_solution.checkout("AAAA"))
        self.assertEquals(195, checkout_solution.checkout("AAABBC"))


