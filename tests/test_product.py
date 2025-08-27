import pytest

from src.product import Product


def test_product_init(product: Product) -> None:
    """Тестируем инициализацию объекта класса Product"""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
