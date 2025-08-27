from src.product import Product


class Category:
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
    products_list: list = []

    def __init__(self, name: str, description: str, products: list):
        """Конструктор для категории товаров"""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
        Category.products_list.extend(products)
