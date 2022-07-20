import inventory
import location_handler


class Entity:
    name = None
    hp = 0
    mhp = 0
    # mp
    atk_ = 0
    def_ = 0
    stamina = 100
    mstamina = 100

    def hurt(self, hp):
        self.hp -= min(hp, self.hp)

    def heal(self, hp):
        self.hp = min(self.mhp, self.hp+hp)

    def tire(self, stamina):
        self.stamina -= min(stamina, self.stamina)

    def rest(self, stamina):
        self.stamina = min(self.mstamina, self.stamina+stamina)

    def use_weapon(self, weapon, victim):
        if weapon.durability >= weapon.durability_deduction:
            weapon.use(self, victim)


class HostileEntity(Entity):
    drops = {}


class Player(Entity):
    stamina = 100
    mstamina = 100
    hp = 100
    mhp = 100
    exp = 0

    def __init__(self):
        self.location = location_handler.Location()
        self.inventory = inventory.Inventory()
        self.combat_moves = []

    def give_item(self, item, amount):
        if item.stackable:
            if self.inventory.find(item, 1):
                self.inventory.slots[self.inventory.find(item, 1)] += amount
            else:
                self.inventory.new_slot(item, amount)
        else:
            for i in range(amount):
                self.inventory.new_slot(item, 1)

    def remove_item(self, item, amount):
        slot_index = self.inventory.find(item, amount)
        if item.stackable and slot_index is not False:
            self.inventory.slots[slot_index].amount -= amount
            if self.inventory.slots[slot_index].amount <= 0:
                self.inventory.slots.pop(slot_index)
        elif not item.stackable:
            for i in range(amount):
                slot_index = self.inventory.find(item, 1)
                if slot_index is not False:
                    self.inventory.slots.pop(slot_index)
