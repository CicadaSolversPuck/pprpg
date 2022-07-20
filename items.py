class Item:
    def __init__(self, name=None, stackable=True):
        self.name = name
        self.cost = 0
        self.information = None
        self.stackable = stackable

    def use(self, *args):
        return False

class Consumable(Item):
    def __init__(self, name=None, stackable=True, heal=0):
        super().__init__(name, stackable)
        self.heal = heal
    
    def action(self, user):
        user.heal(self.heal)
        user.remove_item(self)
        return True

class Weapon(Item):
    def __init__(self, name=None, stackable=False, damage=0, durability=0, pstamina_deduction=0):
        super().__init__(name, stackable)
        self.damage = damage
        self.durability = durability
        self.pstamina_deduction = pstamina_deduction

    def action(self, user, victim):
        user.tire(self.pstamina_deduction)
        victim.hurt(self.damage)
        self.durability -= min(self.pstamina_deduction, self.durability)
        return True

