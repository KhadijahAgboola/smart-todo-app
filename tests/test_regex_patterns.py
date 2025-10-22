# tests/test_regex_patterns.py

import unittest
from src.parsers.regex_patterns import Tags, Priority, Due, Assigned

class TestRegexPatterns(unittest.TestCase):

    def test_tags(self):
        self.assertEqual(Tags.findall("Finish task @home @work"), ['home', 'work'])

    def test_priority(self):
        match = Priority.search("Do homework #high")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), 'high')

    def test_due_date(self):
        match = Due.search("Submit report due:2025-10-12")
        self.assertEqual(match.group(1), '2025-10-12')

    def test_assigned(self):
        match = Assigned.search("assigned:alice@example.com")
        self.assertEqual(match.group(1), 'alice@example.com')

if __name__ == '__main__':
    unittest.main()
