import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
            DigitalVideoDisc("Aladdin")
        ]

    def test_search_existing_title(self):
        result = search_by_title(self.items, "Lion")
        self.assertEqual(len(result), 1)

    def test_search_missing_title(self):
        result = search_by_title(self.items, "Harry Potter")
        self.assertEqual(len(result), 0)

    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

        result = search_by_category(items, "Animation")

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()