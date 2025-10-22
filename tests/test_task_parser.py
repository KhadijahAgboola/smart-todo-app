# tests/test_task_parser.py

import unittest
from src.parsers.task_parser import parse_task_input

class TestTaskParser(unittest.TestCase):

    def test_parse_full_task(self):
        task = 'Complete project @school #high due:2025-10-20 assigned:alice@example.com'
        result = parse_task_input(task)

        self.assertEqual(result['description'], 'Complete project')
        self.assertIn('school', result['tags'])
        self.assertEqual(result['priority'], '#high')
        self.assertEqual(result['due'], '2025-10-20')
        self.assertEqual(result['assigned'], 'alice@example.com')

    def test_parse_with_only_description(self):
        task = 'Buy groceries'
        result = parse_task_input(task)

        self.assertEqual(result['description'], 'Buy groceries')
        self.assertEqual(result['tags'], [])
        self.assertIsNone(result['priority'])

    def test_parse_invalid_tag(self):
        task = 'Do homework @@invalidtag'
        result = parse_task_input(task)

        self.assertIn('invalidtag', result['invalid_tags'])

if __name__ == '__main__':
    unittest.main()
