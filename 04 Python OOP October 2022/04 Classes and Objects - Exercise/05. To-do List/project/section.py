from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for element in self.tasks:
            if element.name == task_name:
                element.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        new_tasks = []
        for element in self.tasks:
            if not element.completed:
                new_tasks.append(element)
        cleared_tasks = len(self.tasks) - len(new_tasks)
        self.tasks = new_tasks
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for element in self.tasks:
            result.append(element.details())
        return "\n".join(result)

