# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
#
# Шаги:
#  1. Создай класс Store:
#  -Атрибуты класса:
#  name: название магазина.
#  address: адрес магазина.#
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#
# Методы класса:
#  __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для items`.
# - метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# - метод для обновления цены товара.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте магазина '{self.name}'")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте магазина '{self.name}'")


store1 = Store("Магазин продуктов 'Зеленая планета'", "ул. Садовая, д. 15")
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)

store2 = Store("Продуктовый магазин 'Свежий выбор'", "пр. Ленина, д. 25")
store2.add_item("Молоко", 1.2)
store2.add_item("Хлеб", 0.8)

store3 = Store("Магазин органических продуктов 'Веган'", "ул. Цветочная, д. 10")
store3.add_item("Орехи", 2.5)
store3.add_item("Овощи", 1.0)

store1.update_item_price("Яблоки", 0.6)
store1.remove_item("Бананы")

print(store1.get_item_price("Яблоки"))
print(store1.get_item_price("Бананы"))
