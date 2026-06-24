from Entity import Entity
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.life = None
        self.firerate = None
        self.score = None

    def move(self):
        pass