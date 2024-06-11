import math
from typing import List, Dict


class InvalidInputException(Exception):
    def __init__(self, exception_msg):
        super().__init__(exception_msg)


class SuperMarketProducts(object):
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product


class Product(object):
    def __init__(self, name, unit_price, special_price_offers, special_qty_offers):
        self.name = name
        self.unit_price = unit_price
        self.special_price_offers = special_price_offers
        self.special_qty_offers = special_qty_offers


# noinspection PyUnusedLocal
# skus = unicode string
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
    supermarket_products = {
        "A": {"price": 50, "special_offer": },
        "B": {"price": 30, "special_offer": {"qty_requirement": 2, "promotion_price": 45}},
        "C": {"price": 20, "special_offer": None},
        "D": {"price": 15, "special_offer": None},
    }
    supermarket_products = SuperMarketProducts()
    supermarket_products.add_product(
        Product("A", 50, {3: 130, 5: 200}, None)
    )
    supermarket_products.add_product(
        Product("B", 30, {2: 45}, None)
    )
    supermarket_products.add_product(
        Product("C", 20, None, None)
    )
    supermarket_products.add_product(
        Product("D", 15, None, None)
    )
    supermarket_products.add_product(
        Product("E", 40, None, {2: 1})
    )

    return supermarket_products


def get_shopping_cart(skus: List[str]) -> Dict:
    shopping_cart = {}

    for sku in skus:
        if sku not in shopping_cart:
            shopping_cart[sku] = 0
        shopping_cart[sku] += 1

    return shopping_cart


def compute_checkout_price(supermarket_products, shopping_cart):
    checkout_price = 0
    for item_id, item_qty in shopping_cart.items():
        unit_price = supermarket_products[item_id]["price"]
        special_offer = supermarket_products[item_id]["special_offer"]

        if special_offer is None:
            checkout_price += unit_price * item_qty
        else:
            qty_requirement = special_offer["qty_requirement"]
            promotion_price = special_offer["promotion_price"]
            number_of_promotions = math.floor(item_qty/qty_requirement)

            checkout_price += (number_of_promotions * promotion_price) + (item_qty - number_of_promotions * qty_requirement) * unit_price

    return checkout_price


def checkout(skus):
    supermarket_products = get_supermarket_products()

    try:
        parsed_skus = parsed_and_validate_input(skus, list(supermarket_products.keys()))
    except Exception:
        return -1

    shopping_cart = get_shopping_cart(parsed_skus)

    return compute_checkout_price(supermarket_products, shopping_cart)


