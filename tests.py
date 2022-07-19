import unittest
import entity
import item_system


class TestInventoryMethods(unittest.TestCase):

    bread = item_system.Item('bread', False)
    rum = item_system.Item('rum')

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


if __name__ == '__main__':
    unittest.main()
