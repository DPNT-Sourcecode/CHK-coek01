from unittest import TestCase


from lib.solutions.HLO import hello_solution


class TestHello(TestCase):
    def test_hello(self):
        self.assertEquals("Hello, World!", hello_solution.hello(""))
