from unittest import TestCase


from lib.solutions.CHK import checkout_solution


class TestHello(TestCase):
    def test_all_items(self):
        self.assertEquals(115, checkout_solution.checkout("ABCD"))

    def test_invalid_input(self):
        self.assertEquals(-1, checkout_solution.checkout(10))

    def test_empty_shopping_cart(self):
        self.assertEquals(0, checkout_solution.checkout(""))

    def test_promotions(self):
        # self.assertEquals(130, checkout_solution.checkout("AAA"))
        # self.assertEquals(180, checkout_solution.checkout("AAAA"))
        # self.assertEquals(195, checkout_solution.checkout("AAABBC"))
        # self.assertEquals(250, checkout_solution.checkout("AAAAAA"))
        # self.assertEquals(330, checkout_solution.checkout("AAAAAAAA"))
        # self.assertEquals(80, checkout_solution.checkout("EE"))
        # self.assertEquals(120, checkout_solution.checkout("EEE"))
        # self.assertEquals(160, checkout_solution.checkout("EEEE"))
        # self.assertEquals(80, checkout_solution.checkout("EEB"))
        # self.assertEquals(120, checkout_solution.checkout("EEEB"))
        # self.assertEquals(160, checkout_solution.checkout("EEEEBB"))
        # self.assertEquals(10, checkout_solution.checkout("F"))
        # self.assertEquals(20, checkout_solution.checkout("FF"))
        # self.assertEquals(20, checkout_solution.checkout("FFF"))
        # self.assertEquals(30, checkout_solution.checkout("FFFF"))
        # self.assertEquals(40, checkout_solution.checkout("FFFFFF"))
        #
        # self.assertEquals(45, checkout_solution.checkout("HHHHH"))
        # self.assertEquals(80, checkout_solution.checkout("HHHHHHHHHH"))
        # self.assertEquals(120, checkout_solution.checkout("KK"))
        # self.assertEquals(120, checkout_solution.checkout("NNNM"))
        # self.assertEquals(200, checkout_solution.checkout("PPPPP"))
        # self.assertEquals(80, checkout_solution.checkout("QQQ"))
        # self.assertEquals(150, checkout_solution.checkout("RRRQ"))
        # self.assertEquals(120, checkout_solution.checkout("UUUU"))
        # self.assertEquals(90, checkout_solution.checkout("VV"))
        # self.assertEquals(130, checkout_solution.checkout("VVV"))
        # self.assertEquals(45, checkout_solution.checkout("STX"))
        # self.assertEquals(45, checkout_solution.checkout("ZZZ"))
        # self.assertEquals(45, checkout_solution.checkout("XYZ"))
        # self.assertEquals(79, checkout_solution.checkout("XXZZZ"))
        self.assertEquals(90, checkout_solution.checkout("STXSTX"))
        self.assertEquals(65, checkout_solution.checkout("SSSZ"))
        self.assertEquals(62, checkout_solution.checkout("STXZ"))








