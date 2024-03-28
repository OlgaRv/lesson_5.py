class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # по умолчанию задача не выполнена


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена")

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                print(f"Задача '{description}' выполнена")
                return
        print(f"Задача '{description}' не найдена")

# функция написана с помощью ИИ
    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(
                    f"Описание: {task.description}, Срок: {task.deadline}, Статус: {'выполнено' if task.status else 'не выполнено'}")
        else:
            print("Нет текущих задач")


task_manager = TaskManager()
task_manager.add_task("Сделать уроки", "01.10.2022")
task_manager.add_task("Сходить в магазин", "05.10.2022")
task_manager.mark_task_as_done("Сделать уроки")
task_manager.get_current_tasks()