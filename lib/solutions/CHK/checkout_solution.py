# noinspection PyUnusedLocal
# skus = unicode string

import math
from collections import OrderedDict
from typing import List, Dict


class InvalidInputException(Exception):
    def __init__(self, exception_msg):
        super().__init__(exception_msg)


class SuperMarketProductsManager(object):
    def __init__(self):
        self.products = {}
        self.same_product_buy_offer = []
        self.buy_product_get_another_for_free_offer = []
        self.buy_various_products_offer = []

    def add_product(self, product):
        self.products[product.name] = product

    def get_available_products(self):
        return list(self.products.keys())

    def add_offer(self, offer):
        if isinstance(offer, SameProductBuyOffer):
            self.same_product_buy_offer.append(offer)

        elif isinstance(offer, BuyVariousProductsOffer):
            self.buy_various_products_offer.append(offer)

        elif isinstance(offer, BuyProductGetAnotherForFreeOffer):
            self.buy_product_get_another_for_free_offer.append(offer)

    def get_checkout_price(self, shopping_cart):
        checkout_price = 0
        for offer in self.buy_product_get_another_for_free_offer:
            offer.apply_offer_if_applicable(checkout_price, shopping_cart)
        for offer in self.buy_various_products_offer:
            offer.apply_offer_if_applicable(checkout_price, shopping_cart)
        for offer in self.same_product_buy_offer:
            offer.apply_offer_if_applicable(checkout_price, shopping_cart)

        for product, checkout_qty in shopping_cart.items():
            checkout_price += self.products[product].get_checkout_price(checkout_qty)


class SameProductBuyOffer(object):
    def __init__(self, target_product, requirement_qty, promo_price):
        self.target_product = target_product
        self.requirement_qty = requirement_qty
        self.promo_price = promo_price

    def apply_offer_if_applicable(self, checkout_price, shopping_cart):
        if self.target_product not in shopping_cart:
            return
        checkout_qty = shopping_cart[self.target_product]
        number_of_promotions = math.floor(checkout_qty / self.requirement_qty)
        checkout_price += (number_of_promotions * self.promo_price)
        shopping_cart[self.target_product] = checkout_qty - number_of_promotions * self.requirement_qty


class BuyProductGetAnotherForFreeOffer(object):
    def __init__(self, target_product, requirement_qty, product_earned):
        self.target_product = target_product
        self.requirement_qty = requirement_qty
        self.product_earned = product_earned

    def apply_offer_if_applicable(self, shopping_cart):
        if self.target_product not in shopping_cart:
            return

        number_of_promotions = math.floor(shopping_cart.get(self.target_product, 0) / self.requirement_qty)
        quantity_of_products_gained = number_of_promotions
        if self.product_earned in shopping_cart:
            if shopping_cart[self.product_earned] > quantity_of_products_gained:
                shopping_cart[self.product_earned] -= quantity_of_products_gained
            else:
                shopping_cart[self.product_earned] = 0


class BuyVariousProductsOffer(object):
    def __init__(self, target_products, requirement_qty, promo_price):
        self.target_products = target_products
        self.requirement_qty = requirement_qty
        self.promo_price = promo_price

    def apply_offer_if_applicable(self, checkout_price, shopping_cart):
        products_bought = 0
        for target_product in self.target_products:
            products_bought += shopping_cart.get(target_product, 0)

        if products_bought < self.requirement_qty:
            return

        num_of_promos = math.floor(products_bought / self.requirement_qty)

        for _ in range(num_of_promos*self.requirement_qty):
            for target_product in self.target_products:
                if shopping_cart.get(target_product, 0) > 0:
                    shopping_cart[target_product] -= 1

        checkout_price += num_of_promos * self.promo_price


class Product(object):
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price

    def get_checkout_price(self, checkout_qty):
        return checkout_qty * self.unit_price

def parsed_and_validate_input(skus: str, available_products: List[str]) -> List[str]:
    if not isinstance(skus, str):
        raise InvalidInputException("Invalid skus type, it must be a string!")

    parsed_skus = []
    for sku in skus:
        if sku not in available_products:
            raise InvalidInputException("Invalid product informed: " + sku)

        parsed_skus.append(sku)
    return parsed_skus


def get_supermarket_products_manager():
    supermarket_products = SuperMarketProductsManager()
    supermarket_products.add_product(Product("A", 50))
    supermarket_products.add_product(Product("B", 30))
    supermarket_products.add_product(Product("C", 20))
    supermarket_products.add_product(Product("D", 15))
    supermarket_products.add_product(Product("E", 40))
    supermarket_products.add_product(Product("F", 10))
    supermarket_products.add_product(Product("G", 20))
    supermarket_products.add_product(Product("H", 10))
    supermarket_products.add_product(Product("I", 35))
    supermarket_products.add_product(Product("J", 60))
    supermarket_products.add_product(Product("K", 70))
    supermarket_products.add_product(Product("L", 90))
    supermarket_products.add_product(Product("M", 15))
    supermarket_products.add_product(Product("N", 40))
    supermarket_products.add_product(Product("O", 10))
    supermarket_products.add_product(Product("P", 50))
    supermarket_products.add_product(Product("Q", 30))
    supermarket_products.add_product(Product("R", 50))
    supermarket_products.add_product(Product("S", 20))
    supermarket_products.add_product(Product("T", 20))
    supermarket_products.add_product(Product("U", 40))
    supermarket_products.add_product(Product("V", 50))
    supermarket_products.add_product(Product("W", 20))
    supermarket_products.add_product(Product("X", 17))
    supermarket_products.add_product(Product("Y", 20))
    supermarket_products.add_product(Product("Z", 21))
    SameProductBuyOffer


    return supermarket_products


def get_shopping_cart(skus: List[str]) -> Dict:
    shopping_cart = {}

    for sku in skus:
        if sku not in shopping_cart:
            shopping_cart[sku] = 0
        shopping_cart[sku] += 1

    return shopping_cart


def compute_checkout_price(supermarket_products: SuperMarketProductsManager, shopping_cart: Dict):
    checkout_price = 0
    supermarket_products.apply_special_product_offers(shopping_cart)

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

