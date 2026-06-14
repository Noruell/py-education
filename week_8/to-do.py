class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            return f"[X] {self.title}"
        else:
            return f"[ ] {self.title}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def remove_task(self, index):
        if 0 <= index - 1 < len(self.tasks):
            del self.tasks[index - 1]

    def complete_task(self, index):
        if 0 <= index - 1 < len(self.tasks):
            self.tasks[index - 1].complete()
    
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст!")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Собрать вещи")
    todo.add_task("Сесть в машину")
    todo.add_task("Доехать до Ташары")

    todo.complete_task(1)   # завершаем первую задачу

    todo.show_tasks()