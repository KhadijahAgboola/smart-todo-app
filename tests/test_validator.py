# tests/test_validator.py

import unittest
from src.parsers.validator import TaskValidator

class TestValidator(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(TaskValidator.is_valid_date('2025-12-31'))
        self.assertFalse(TaskValidator.is_valid_date('31-12-2025'))

    def test_valid_priority(self):
        self.assertTrue(TaskValidator.is_valid_priority('#high'))
        self.assertFalse(TaskValidator.is_valid_priority('#urgent'))

    def test_valid_tag(self):
        self.assertTrue(TaskValidator.is_valid_tag('@work'))
        self.assertFalse(TaskValidator.is_valid_tag('@invalid tag'))

    def test_valid_task_id(self):
        self.assertTrue(TaskValidator.is_valid_task_id(5))
        self.assertFalse(TaskValidator.is_valid_task_id(-1))

if __name__ == '__main__':
    unittest.main()
