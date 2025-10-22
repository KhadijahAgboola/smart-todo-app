# tests/test_date_parser.py

import unittest
from src.parsers.date_parser import convert_human_date

class TestDateParser(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(convert_human_date('2025-01-10'), '2025-01-10')

    def test_tomorrow(self):
        result = convert_human_date('tomorrow')
        self.assertIsNotNone(result)  # Not testing exact date to avoid time dependency

    def test_next_week(self):
        result = convert_human_date('next week')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
