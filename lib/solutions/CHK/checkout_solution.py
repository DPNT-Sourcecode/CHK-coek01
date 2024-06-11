# noinspection PyUnusedLocal
# skus = unicode string

import math
from collections import OrderedDict
from typing import List, Dict


class InvalidInputException(Exception):
    def __init__(self, exception_msg):
        super().__init__(exception_msg)


class SuperMarketProducts(object):
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def get_available_products(self):
        return list(self.products.keys())

    def get_checkout_price_for_product(self, product, checkout_qty):
        return self.products[product].get_checkout_price(checkout_qty)


class Product(object):
    def __init__(self, name, unit_price, special_price_offers):
        self.name = name
        self.unit_price = unit_price
        self.special_price_offers = special_price_offers

    def get_checkout_price(self, checkout_qty):
        if self.special_price_offers is None:
            return checkout_qty * self.unit_price

        checkout_price = 0
        for special_offer_qty_requirement, special_price in self.special_price_offers.items():
            number_of_promotions = math.floor(checkout_qty/special_offer_qty_requirement)
            checkout_price += (number_of_promotions * special_price)
            checkout_qty = checkout_qty - number_of_promotions * special_offer_qty_requirement

        checkout_price += checkout_qty * self.unit_price
        return checkout_price


def parsed_and_validate_input(skus: str, available_products: List[str]) -> List[str]:
    if not isinstance(skus, str):
        raise InvalidInputException("Invalid skus type, it must be a string!")

    parsed_skus = []
    for sku in skus:
        if sku not in available_products:
            raise InvalidInputException("Invalid product informed: " + sku)

        parsed_skus.append(sku)
    return parsed_skus


def get_supermarket_products():
    supermarket_products = SuperMarketProducts()

    special_price_offers_product_A = OrderedDict()
    special_price_offers_product_A[5] = 200
    special_price_offers_product_A[3] = 130
    supermarket_products.add_product(
        Product("A", 50, {3: 130, 5: 200})
    )
    supermarket_products.add_product(
        Product("B", 30, {2: 45})
    )
    supermarket_products.add_product(
        Product("C", 20, None,)
    )
    supermarket_products.add_product(
        Product("D", 15, None)
    )
    supermarket_products.add_product(
        Product("E", 40, {3: 80})
    )

    return supermarket_products


def get_shopping_cart(skus: List[str]) -> Dict:
    shopping_cart = {}

    for sku in skus:
        if sku not in shopping_cart:
            shopping_cart[sku] = 0
        shopping_cart[sku] += 1

    return shopping_cart


def compute_checkout_price(supermarket_products: SuperMarketProducts, shopping_cart: Dict):
    checkout_price = 0
    for item_id, item_qty in shopping_cart.items():
        checkout_price += supermarket_products.get_checkout_price_for_product(item_id, item_qty)

    return checkout_price


def checkout(skus):
    supermarket_products = get_supermarket_products()

    try:
        parsed_skus = parsed_and_validate_input(skus, supermarket_products.get_available_products())
    except Exception:
        return -1

    shopping_cart = get_shopping_cart(parsed_skus)

    return compute_checkout_price(supermarket_products, shopping_cart)



