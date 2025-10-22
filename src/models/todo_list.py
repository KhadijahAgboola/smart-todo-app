from src.models.task import Task
from src.services.storage_service import Storage
from src.parsers.task_parser import parse_task_input

class TaskManagement:     #Initiating the Task Management
    def __init__(self):
        self.tasks=[]
        self.storage=Storage()

    def add_task(self, content):
        parse = parse_task_input(content)
        task=Task(content=parse["description"],
            tags=parse["tags"],
            priority=parse["priority"],
            due=parse["due"],
            assigned=parse["assigned"],
            time=parse["time"],
            duration=parse["duration"])
        self.tasks.append(task)     #adding all task to tasks
        self.storage.save_tasks(self.tasks)
    
    def list_tasks(self):
        for task in self.tasks:
            print(task.display())

    
    def delete_task(self, id):     #defining the delete method to take note ID
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"------------------------------------------\nTask with ID {id} has been deleted.\n------------------------------------------")
            else:
                print(f"------------------------------------------\nNo task with ID  {id}\n------------------------------------------")
        self.storage.save_tasks(self.tasks)


    def update_task(self, id):
        for task in self.tasks:
            if task.id == id:
                updated_task=input("Enter the update: ")
                task=updated_task
                print(f"------------------------------------------\nTask with ID {id} has been updated to .\n {task}")
            else:
                print(f"------------------------------------------\nNo task with ID {id}")
        self.storage.save_tasks(self.tasks)
                      
    
    def complete_task(self, id):
        for task in self. tasks:
            if task.id == id:
                task.completed = True
                self.storage.save_tasks(self.tasks)
            print(task.display())
        self.storage.save_tasks(self.tasks)

    def search_by_keyword(self, keyword):
        pattern = re.compile(keyword, re.IGNORECASE)
        return [task for task in self.tasks if pattern.search(task.content)]

    # ---- Filter by @tags ----
    def filter_by_tags(self, tag_name):
        return [task for task in self.tasks if task.tags and tag_name in task.tags]

    # ---- Filter by priority (#high, #medium, #low) ----
    def filter_by_priority(self, priority_level):
        return [task for task in self.tasks if task.priority and task.priority.lower() == priority_level.lower()]

    # ---- Filter by due date (regex matches) ----
    def filter_by_due_date(self, due_pattern):
        pattern = re.compile(due_pattern, re.IGNORECASE)
        return [task for task in self.tasks if task.due and pattern.search(task.due)]

    # ---- Filter by assigned email ----
    def filter_by_assigned(self, email):
        return [task for task in self.tasks if task.assigned and task.assigned.lower() == email.lower()]