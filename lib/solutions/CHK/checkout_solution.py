

# noinspection PyUnusedLocal
# skus = unicode string

class Item(object):
    def __init__(self, item_id, unit_price, special_offers):
        self.item_id = item_id
        self.unit_price = unit_price
        self.special_offers = special_offers

def get_parsed_skus(skus):
    if not isinstance(skus, str):
        raise Exception("Invalid skus type, it must be a string")

    parsed_skus = []
    for sku in skus:
        parsed_skus.append(sku)
    return parsed_skus


def checkout(skus):
    try:
        parsed_skus = get_parsed_skus(skus)
    except Exception as e:
        return -1

    total_price = 0

    items = {
        "A": {"price": 50, "special_offer": {3: 130}},
        "B": {"price": 30, "special_offer": {2: 45}},
        "C": {"price": 20, "special_offer": {}},
        "D": {"price": 15, "special_offer": {}},
    }

    shopping_cart = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for sku in parsed_skus:
        if sku not in items:
            return -1

        shopping_cart[sku] += items[sku]

    for item in shopping_cart.items():
        unit_price = items[item]["price"]
        special_offer = items[item]["special_offer"]
        if



