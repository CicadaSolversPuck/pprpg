import entity
import item_system

puck = entity.Player()

bread = item_system.Item('bread')
rum = item_system.Item('rum')


def inventory_test():
    puck.give_item(bread, 20)

    puck.remove_item(bread, 20)

    puck.inventory.display()


inventory_test()
