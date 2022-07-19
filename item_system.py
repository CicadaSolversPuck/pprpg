class Inventory:
    slots = []
    vassus = 0

    def find(self, item, amount):
        n = -1
        for slot in self.slots:
            n += 1
            if slot.item is item and slot.amount >= amount:
                return n
        return False

    def new_slot(self, item, amount):
        self.slots.append(Slot(item, amount))


# remove end comma

    def display(self):
        print('Inventory')
        print('-'*30)
        print(f'Vassus: {self.vassus}')
        print('Items: ', end='')
        for slot in self.slots:
            print(f'{slot.item.name}(x{slot.amount})', end=', ')
        print()
        print('-'*30)


class Slot:
    def __init__(self, item=None, amount=0):
        self.item = item
        self.amount = amount


class DurabilitySlot(Slot):
    def __init__(self):
        super()
        durability = int(self.item.durability)
        number_of_uses = int(self.item.number_of_uses)


class Item:
    def __init__(self, name=None, stackable=True):
        self.name = name
        self.cost = 0
        self.information = None
        self.stackable = stackable

    def use(self, *args):
        return False


class Weapon(Item):
    damage = 0
    durability = 0
    durability_deduction = 0
    pstamina_deduction = 0
    stackable = False

    def action(self, user, victim):
        user.tire(self.pstamina_deduction)
        victim.hurt(self.damage)
        self.durability -= min(self.pstamina_deduction, self.durability)
        return True
