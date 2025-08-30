import pytest


from src.category import Category

def test_category(first_category: Category, second_category: Category) -> None:
    """Тестируем инициализацию объекта класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций"
    )
    assert len(first_category.products_in_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products_property(first_category: Category) -> None:
    """Тестируем геттер, который возвращает строку со всеми продуктами в приватном атрибуте products"""
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

def test_category_middle_price(first_category: Category) -> None:
    """Тестируем метод, который подсчитывает средний ценник всех товаров в данной категории,
    в том числе и случай, когда в категории нет товаров"""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert first_category.middle_price() == 111629.63
    assert category_empty.middle_price() == 0

def test_category_str(second_category: Category) -> None:
    """Тестируем строковое отображение товаров в категории"""
    assert str(second_category) == "Телевизоры, количество продуктов: 7 шт."


def test_category_add_product_invalid(first_category: Category) -> None:
    """Тестируем поведение метода добавления продукта в атрибут products при попытке добавить вместо
    продукта другой объект - вызываем ошибку"""
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")





