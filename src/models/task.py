import datetime     #this is necessary because of the timestamp


class Task:
    id = 1  
    def __init__(self, content, tags=None, priority=None, due=None, assigned=None, time=None, duration=None, frequency=None):
        self.id=Task.id
        Task.id += 1
        self.content = content
        self.tags=tags
        self.priority=priority
        self.due=due
        self.assigned=assigned
        self.time=time
        self.duration=duration
        self.frequency=frequency
        self.completed = False
        #self.created_at=datetime.datetime.now()     #this adds current timestamp to each note added

    
    def display(self):
        status = "✔️ " if self.completed else "⚪"
        info = f"------------------------------------------\n{status} ID: {self.id} | {self.content}"
        if self.tags:
            info += f" | Tags: {', '.join(self.tags)}"
        if self.priority:
            info += f" | Priority: {self.priority}"
        if self.due:
            info += f" | Due: {self.due}"
        if self.assigned:
            info += f" | Assigned: {self.assigned}"
        if self.time:
            info += f" | Time: {self.time}"
        if self.duration:
            info += f" | Duration: {self.duration}"
        if self.frequency:
            info += f" | Frequency: {self.frequency}"
        return info

            

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
    
