from ball import Ball


class Team:

    @property
    def ball(self):
        return self._ball

    def __init__(self, color):
        self._color = color
        self._ball = []

        for i in range(1, 8):
            self._ball.append(Ball(i))
