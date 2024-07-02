import random
from constants import item_names, categories


def generate_products(min_price: int, max_price: int, num_products: int) -> list:
    """
    Generates a list of products with random categories, item names, and prices.
    """
    products = []

    for product_id in range(1, num_products):
        category = random.choice(categories)
        item_name = random.choice(item_names)
        price = round(random.uniform(min_price, max_price), 2)
        products.append(
            {
                "product_id": product_id,
                "category": category,
                "item": item_name,
                "price": price,
            }
        )

    return products


# Example usage
if __name__ == "__main__":
    min_price = 4
    max_price = 150
    num_products = 30
    generated_products = generate_products(min_price, max_price, num_products)
    print(generated_products)
