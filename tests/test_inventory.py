# This is an inventory system, changes made here might change at any time, this is not finished
print("go away this isnt finished")


class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def __str__(self):
        out = '\t'.join(['Name', 'Attack', 'Armor', 'Weight', 'Value'])
        for item in self.items.values():
            out += '\n' + '\t'.join([
                str(x) for x in
                [item.name, item.attack, item.armor, item.weight, item.price]
            ])
        return out


inventory = Inventory()
inventory.add_item(Item('Sword', 5, 1, 15, 2))
inventory.add_item(Item('Armor', 0, 10, 25, 5))
print(inventory)


def test_inventory():
    inventory = Inventory()
    pass
