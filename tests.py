import unittest
import entity
import inventory
import items

class TestInventoryMethods(unittest.TestCase):

    bread = items.Item('bread', False)
    rum = items.Item('rum')

    def test_add_item(self):
        puck = entity.Player()
        puck.give_item(self.bread, 1)
        self.assertEqual(puck.inventory.slots[0].item, self.bread)

    def test_remove_unstackable_item(self):
        puck = entity.Player()
        puck.give_item(self.bread, 20)
        puck.remove_item(self.bread, 20)
        self.assertEqual(puck.inventory.slots, [])

    def test_remove_stackable_item(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        puck.remove_item(self.rum, 20)
        self.assertEqual(puck.inventory.slots, [])

    def test_remove_some_stackable_item(self):
        puck = entity.Player()
        puck.give_item(self.rum, 20)
        puck.remove_item(self.rum, 10)
        self.assertEqual(puck.inventory.slots[0].amount, 10)


if __name__ == '__main__':
    unittest.main()
