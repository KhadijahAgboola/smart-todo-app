# src/parsers/validator.py
import re
from src.parsers.regex_patterns import Priority, Tags, Due

class TaskValidator:

    @staticmethod
    def is_valid_date(date_str):
        """Validates YYYY-MM-DD format"""
        return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))

    @staticmethod
    def is_valid_priority(priority):
        """Validates #high #medium #low"""
        return bool(Priority.match(priority))

    @staticmethod
    def is_valid_tag(tag):
        """Validates @tag format with letters, numbers, _ and -"""
        return bool(Tags.match(tag))

    @staticmethod
    def is_valid_task_id(task_id):
        """Validates that ID is a number"""
        return str(task_id).isdigit()
