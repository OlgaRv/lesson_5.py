# вариант преподавателя
class Task_M():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, dedline):
        self.tasks.append({'description' : description,
                           'dedline' :dedline,
                           'status': "не выполнено"})
        print(f"Задача {description} добавлена")
    def mark_task(self, description):
        for task in  self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                print(f"Задача {description} выполнена")
                return
            else:
                print(f"Задача {description} не выполнена")

    def show_task(self):
            print("Текущие задачи")
            for task in self.tasks:
                if task['status'] == "не выполнено":
                    print(f"{task['description']} - {task['dedline']}")

t = Task_M()
t.add_task("Прочитать книгу", "01.04.2024")
t.add_task("Пробежать марафон", "05.04.2024")
t.add_task("Починить машину", "10.04.2024")

t.show_task()

t.mark_task("Прочитать книгу")