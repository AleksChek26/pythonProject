import pytest

from src.product import Product
from src.category import Category


def test_product_init(product: Product) -> None:
    """Тестируем инициализацию объекта класса Product"""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_new_product_different( first_category: Category) -> None:
    """Тестируем метод, который принимает на вход параметры отличного от других наименований товара и возвращает
    созданный объект класса Product"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S32 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 5,
        },
        first_category.products_list,
    )
    assert new_product.name == "Samsung Galaxy S32 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180010.0
    assert new_product.quantity == 5

def test_product_str(product: Product) -> None:
    """Тестируем строковое отображение продукта"""
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_init_invalid() -> None:
    """Тестируем поведение конструктора при попытке добавить товар разного класса с нулевым количеством, то есть
    вызываем исключение ValueError"""
    with pytest.raises(ValueError) as e1:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        assert str(e1.value) == "Товар с нулевым количеством не может быть добавлен"

def test_product_add(product: Product, other_product: Product) -> None:
    """Тестируем метод получения полной стоимости всех выбранных товаров на складе"""
    assert product + other_product == 2580000
