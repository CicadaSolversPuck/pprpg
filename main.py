import entity
import data.consumables

puck = entity.Player()

bread = data.consumables.bread


def inventory_test():
    puck.give_item(bread, 20)

    puck.inventory.display()


inventory_test()
