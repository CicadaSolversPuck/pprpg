import item_system
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

    combat_moves = []
    drops = {}


class Player(Entity):
    inventory = item_system.Inventory()
    stamina = 100
    mstamina = 100
    combat_moves = []
    hp = 100
    mhp = 100
    exp = 0
    location = location_handler.Location()

    def give_item(self, item, amount):
        if self.inventory.find(item, 1) and item.stackable:
            self.inventory.slots[self.inventory.find(item, 1)] += amount
        else:
            for i in range(amount):
                self.inventory.new_slot(item, 1)

    def remove_item(self, item, amount):
        if self.inventory.find(item, 1) is not True and item.stackable:
            self.inventory.slots[self.inventory.find(
                item, amount+1)].amount -= amount
        else:
            del self.inventory.slots[self.inventory.find(item, 1)]
