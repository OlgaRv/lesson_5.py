# Менеджер задач
# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False
class TaskManager():
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

    def get_current_tasks(self):
        current_tasks = []
        for task in self.tasks:
            if task.status == False:
                current_tasks.append(task)
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(f"Описание: {task.description}, Срок: {task.deadline}, Статус: не выполнено")
        else:
            print("Нет текущих задач")


task_manager = TaskManager()
task_manager.add_task("Сходить в магазин", "29.03.2024")
task_manager.add_task("Погулять с собакой", "29.03.2024")
task_manager.add_task("Вынести мусор", "30.03.2024")
task_manager.mark_task_as_done("Погулять с собакой")
# task_manager.mark_task_as_done("Сходить в магазин")
# task_manager.mark_task_as_done("Вынести мусор")
task_manager.get_current_tasks()