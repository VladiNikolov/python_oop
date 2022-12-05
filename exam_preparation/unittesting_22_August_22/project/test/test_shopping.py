from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShopping(TestCase):


    def test_correct_initializing(self):
        shop = ShoppingCart("Magazin", 200)
        self.assertEqual("Magazin", shop.shop_name)
        self.assertEqual(100, shop.budget)
        self.assertEqual({}, shop.products)

    def test_invalid_shop_name(self):
        with self.assertRaises(ValueError) as ve:
            shop = ShoppingCart("Magazin1", 100)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_card_raise_exception(self):
        shop = ShoppingCart("Magazin", 200)
        with self.assertRaises(ValueError) as ve:
            shop.add_to_cart("test_product", 100)

        self.assertEqual(f"Product test_product cost too much!", str(ve.exception))

    def test_add_to_card_with_valid_data(self):
        shop = ShoppingCart("Magazin", 200)
        shop.add_to_cart("name_product1", 90)
        self.assertEqual("name_product2 product was successfully added to the cart!", shop.add_to_cart("name_product2", 98))
        self.assertEqual({"name_product1": 90, "name_product2": 98}, shop.products)

    def test_remove_from_card_raise_exception(self):
        shop = ShoppingCart("Magazin", 200)
        with self.assertRaises(ValueError) as ve:
            shop.remove_from_cart("name_product1")
        self.assertEqual(f"No product with name name_product1 in the cart!", str(ve.exception))

    def test_remove_from_card_valid_data(self):
        shop = ShoppingCart("Magazin", 200)
        shop.add_to_cart("name_product1", 90)
        shop.add_to_cart("name_product2", 99)
        result = shop.remove_from_cart("name_product1")
        expected = f"Product name_product1 was successfully removed from the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({"name_product2": 99}, shop.products)

    def test_add_method(self):
        first = ShoppingCart("Magazin", 200)
        first.add_to_cart("from_shop", 1)
        second = ShoppingCart("MagazinTwo", 100)
        second.add_to_cart("from_shop2", 2)
        merged = first.__add__(second)
        self.assertEqual("MagazinMagazinTwo", merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({"from_shop": 1, "from_shop2": 2}, merged.products)

    def test_buy_product_raise_exception(self):
        shop = ShoppingCart("Magazin", 20)
        shop.add_to_cart("name_product1", 99)
        with self.assertRaises(ValueError) as ve:
            shop.buy_products()
        expected = "Not enough money to buy the products! Over budget with 79.00lv!"
        actual = str(ve.exception)
        self.assertEqual(expected, actual)

    def test_bye_product_valid_data(self):
        shop = ShoppingCart("Magazin", 200)
        shop.add_to_cart("name_product1", 90)
        shop.add_to_cart("name_product2", 98)
        self.assertEqual(f'Products were successfully bought! Total cost: 188.00lv.', shop.buy_products())


if __name__ == '__main__':
    main()