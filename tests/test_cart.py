import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        dvd_21 = DigitalVideoDisc("DVD 21")

        self.assertFalse(cart.add_dvd(dvd_21))
        self.assertEqual(len(cart.items), 20)

    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD", cost=100))

        self.assertAlmostEqual(
            cart.total_cost_with_discount(20),
            80
        )

    def test_invalid_discount(self):
        cart = Cart()

        for percent in (-10, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    cart.total_cost_with_discount(percent)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars"))
        cart.add_dvd(DigitalVideoDisc("Aladdin"))

        result = cart.sort_by_title()

        self.assertEqual(
            [item.title for item in result],
            ["Aladdin", "Star Wars"]
        )

        # Thứ tự trong giỏ hàng vẫn giữ nguyên.
        self.assertEqual(
            [item.title for item in cart.items],
            ["Star Wars", "Aladdin"]
        )

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=30))
        cart.add_dvd(DigitalVideoDisc("B", cost=10))

        result = cart.sort_by_cost()

        self.assertEqual(
            [item.cost for item in result],
            [10, 30]
        )

        # Thứ tự trong giỏ hàng vẫn giữ nguyên.
        self.assertEqual(
            [item.cost for item in cart.items],
            [30, 10]
        )


if __name__ == "__main__":
    unittest.main()