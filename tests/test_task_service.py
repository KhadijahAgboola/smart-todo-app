# tests/test_task_service.py

import unittest
from src.services.task_service import TaskService

class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.manager = TaskService()
        self.manager.add_task('Complete assignment @school')

    def test_add_task(self):
        self.assertEqual(len(self.manager.tasks), 1)

    def test_mark_complete(self):
        self.manager.complete_task(1)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_search_by_tag(self):
        results = self.manager.search_by_tag('school')
        self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()
