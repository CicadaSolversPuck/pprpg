import entity
import item_system

puck = entity.Player()

bread = item_system.Item('bread', False)
rum = item_system.Item('rum')


def inventory_test():
    puck.give_item(bread, 20)
    puck.give_item(rum, 2)

    if puck.inventory.find(bread, 20) is not True:
        puck.inventory.display()
        puck.remove_item(bread, 18)

    puck.inventory.display()


inventory_test()
