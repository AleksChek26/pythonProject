import pytest


from src.category import Category


def test_category(first_category: Category, second_category: Category) -> None:
    """Тестируем инициализацию объекта класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций"
    )

    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.product_count == 4
