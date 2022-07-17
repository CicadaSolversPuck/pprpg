class Inventory:
    items = {}
    vassus = 0

    def check_item(self, item, amount):
        if item in self.items.keys() and self.items[item] >= amount:
            return True
        return False

    def add_item(self, item, amount):
        if self.check_item(item, 1):
            self.items[item] += amount
        else:
            self.items[item] = amount

    def remove_item(self, item, amount):
        self.items[item] -= amount
        if self.items[item] == 0:
            del self.items[item]
