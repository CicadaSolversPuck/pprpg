class Item:
    def __init__(self, name=None, stackable=True):
        self.name = name
        self.cost = 0
        self.information = None
        self.stackable = stackable

    def use(self, *args):
        return False

class Consumable(Item):
    def __init__(self, heal):
        self.heal = heal
    
    def action(self, user):
        user.heal(self.heal)
        user.remove_item(self)
        return True

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

