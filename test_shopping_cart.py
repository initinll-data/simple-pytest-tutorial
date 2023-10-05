from unittest.mock import Mock

import pytest

from item_database import ItemDatabase
from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    # All setup for cart here..
    return ShoppingCart(3)


def test_can_add_item_to_cart(cart: ShoppingCart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart: ShoppingCart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart: ShoppingCart):
    for _ in range(3):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price(cart: ShoppingCart):
    cart.add("apple")
    cart.add("orange")

    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_database) == 3.0
