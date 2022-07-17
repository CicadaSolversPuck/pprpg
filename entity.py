import item_system


class Entity:
    name = None
    hp = 0
    # mp
    atk_ = 0
    def_ = 0
    drops = {}


class HostileEntity(Entity):
    stamina = 100
    combat_moves = []


class Player(HostileEntity):
    inventory = item_system.Inventory()
