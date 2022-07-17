import entity

puck = entity.Player()
puck.inventory.add_item('bread', 20)

if puck.inventory.check_item('bread', 20):
    puck.inventory.remove_item('bread', 20)

print(puck.inventory.items)
