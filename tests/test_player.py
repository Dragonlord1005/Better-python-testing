class Player:
    def __init__(self, gold, health):
        """Inititates stuff"""
        self.gold = gold
        self.health = health

    def get_gold(self):
        return self.gold


def test_player():
    joe = Player(1, 20)
    assert print(joe.get_gold()) != 1
