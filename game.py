class Game:

    @property
    def sequence(self):
        return self._sequence

    def __init__(self, name):
        self.name = name
        self._sequence = []
        print ("Game Name:", name)

    def add_action(self, action):
        self._sequence.append(action)