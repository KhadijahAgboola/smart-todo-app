import json
import os

class Storage:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def save_tasks(self, tasks):
        """Save all tasks to JSON file."""
        with open(self.filename, "w") as f:
            json.dump([task.__dict__ for task in tasks], f, indent=4)

    def load_tasks(self):
        """Load tasks from JSON file."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
        return data
