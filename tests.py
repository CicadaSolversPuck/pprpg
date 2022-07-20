import unittest
import entity
import inventory
import items


class TestInventoryMethods(unittest.TestCase):

    bread = items.Item('bread', False)
    rum = items.Item('rum')

    def test_add_stackable_item(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        self.assertEqual(puck.inventory.slots[0].amount, 20)
        self.assertEqual(puck.inventory.slots[0].item, self.rum)

    def test_add_unstackable_item(self):
        puck = entity.Player()
        puck.give_item(self.bread, 20)
        for i in range(20):
            self.assertEqual(puck.inventory.slots[i].item, self.bread)

    def test_remove_unstackable_item(self):
        puck = entity.Player()
        puck.give_item(self.bread, 20)
        puck.remove_item(self.bread, 20)
        self.assertEqual(puck.inventory.slots, [])

    def test_remove_unstackable_item_not_in_inventory(self):
        puck = entity.Player()
        puck.give_item(self.bread, 20)
        with self.assertRaises(ValueError):
            puck.remove_item(self.rum, 20)
        for i in range(20):
            # this is returning None. Figure out why.
            self.assertEqual(puck.inventory.slots[i].item, self.bread)

    def test_remove_stackable_item(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        puck.remove_item(self.rum, 20)
        self.assertEqual(puck.inventory.slots, [])

    def test_remove_item_not_in_inventory(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        with self.assertRaises(ValueError):
            puck.remove_item(self.bread, 20)

    def test_remove_item_not_enough_in_inventory(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        puck.remove_item(self.rum, 30)
        # It's not removing the item from the inventory.
        self.assertEqual(puck.inventory.slots, [])

    def test_remove_some_stackable_item(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        puck.remove_item(self.rum, 10)
        self.assertEqual(puck.inventory.slots[0].amount, 10)


class TestPlayerMethods(unittest.TestCase):

    def test_hurt(self):
        puck = entity.Player()
        puck.hurt(10)
        self.assertEqual(puck.hp, 90)

    def test_hurt_when_dead(self):
        puck = entity.Player()
        puck.hp = 0
        puck.hurt(10)
        self.assertEqual(puck.hp, 0)

    def test_heal(self):
        puck = entity.Player()
        puck.hp = 90
        puck.heal(10)
        self.assertEqual(puck.hp, 100)

    def test_heal_when_full(self):
        puck = entity.Player()
        puck.heal(10)
        self.assertEqual(puck.hp, 100)

    def test_tire(self):
        puck = entity.Player()
        puck.tire(10)
        self.assertEqual(puck.stamina, 90)

    def test_tire_when_tired(self):
        puck = entity.Player()
        puck.stamina = 0
        puck.tire(10)
        self.assertEqual(puck.stamina, 0)

    def test_rest(self):
        puck = entity.Player()
        puck.stamina = 90
        puck.rest(10)
        self.assertEqual(puck.stamina, 100)

    def test_rest_when_rested(self):
        puck = entity.Player()
        puck.rest(10)
        self.assertEqual(puck.stamina, 100)

    def test_use_weapon(self):
        puck = entity.Player()
        puck.give_item(items.Weapon('sword', 10, 10, 10, 10), 1)
        puck.use_weapon(puck.inventory.slots[0].item, entity.HostileEntity())
        self.assertEqual(puck.inventory.slots[0].amount, 9)


if __name__ == '__main__':
    unittest.main()
