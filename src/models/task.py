import datetime     #this is necessary because of the timestamp
from src.services.storage_service import Storage

class Task:
    id = 1  
    def __init__(self, content):
        self.id=Task.id
        Task.id += 1
        self.content = content
        self.completed = False
        #self.created_at=datetime.datetime.now()     #this adds current timestamp to each note added

    
    def display(self):
        status = "✔️ " if self.completed else "❌"
        return f"------------------------------------------\n{status} ID: {self.id} {self.content}" #created at {self.created_at}

class TaskManagement:     #Initiating the Task Management
    def __init__(self):
        self.tasks=[]
        self.storage=Storage()

    def add_task(self, content):
        task=Task(content)
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
            

    '''def search_notes(self, keyword):
        result=[]
        for note in self.notes:
            if keyword in note.content:
                result.append(note)
            
        if not result:
            print(f"No note contain  {keyword}")
        else:
            for note in result:
                print(note.display())'''
    
#Use case
todo = TaskManagement()
todo.add_task("Finish my report")
todo.add_task("Buy groceries")
todo.list_tasks()
'''delt=int(input("enter the id: "))
todo.delete_task(delt)
updt=int(input("enter the id: "))
todo.update_task(updt)'''
com= int(input("enter the id: "))
todo.complete_task(com)