import math
from typing import List


class InvalidInputException(Exception):
    def __init__(self, exception_msg):
        super().__init__(exception_msg)

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
        "A": {"price": 50, "special_offer": {"qty_requirement": 3, "promotion_price": 130}},
        "B": {"price": 30, "special_offer": {"qty_requirement": 2, "promotion_price": 45}},
        "C": {"price": 20, "special_offer": None},
        "D": {"price": 15, "special_offer": None},
    }
    return supermarket_products


def checkout(skus):
    supermarket_products = get_supermarket_products()

    try:
        parsed_skus = parsed_and_validate_input(skus, supermarket_products.keys())

    except Exception:
        return -1



    shopping_cart = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for sku in parsed_skus:
        if sku not in items:
            return -1

        shopping_cart[sku] += 1

    total_price = 0
    for item_id, item_qty in shopping_cart.items():
        unit_price = items[item_id]["price"]
        special_offer = items[item_id]["special_offer"]

        if special_offer is None:
            total_price += unit_price * item_qty
        else:
            qty_requirement = special_offer["qty_requirement"]
            promotion_price = special_offer["promotion_price"]
            number_of_promotions = math.floor(item_qty/qty_requirement)

            total_price += (number_of_promotions * promotion_price) + (item_qty - number_of_promotions * qty_requirement) * unit_price

    return total_price

