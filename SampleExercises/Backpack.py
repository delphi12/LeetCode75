class Backpack:

    def __init__(self, items):
        self.items = []

    def add_item(self, i):
        self.items.append(i)

    def has_item(self, i):
         return i in self.items

    def remove_item(self, i):
        if i in self.items:
            self.items.remove(i)
        else:
            print("Item not in backpack")

