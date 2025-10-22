from src.models.todo_list import TaskManagement
from src.parsers.regex_patterns import Tags, Priority, Due, Assigned, Time, Duration

#Use case
todo = TaskManagement()
todo.add_task("Review PRs every Monday @work 1h assigned:alex@gmail.com")
todo.add_task("Call doctor tomorrow at 2pm @personal")
todo.add_task("Complete project @school #high due:2025-10-20 assigned to alice")
todo.list_tasks()
'''delt=int(input("enter the id: "))
todo.delete_task(delt)
updt=int(input("enter the id: "))
todo.update_task(updt)'''
com= int(input("enter the id: "))
todo.complete_task(com)
search=input("enter the tags: ")
results = todo.filter_by_priority(search)
if results:
    for task in results:
         print(task.display())
else:
    print(f"No task found with tag: {search}")