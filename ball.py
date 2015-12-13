import sys

class Ball:

    @property
    def number(self):
        return self._number

    @property
    def status(self):
        return self._status

    @property
    def active_hit_list(self):
        return self._active_hit

    def __init__(self, number):
        self._number = number
        self._status = 0
        self._foul = 0
        self._misshit = 0
        self._hit_record = []
        self._get_hit_by = []
        self._active_hit = []

    def __increase_status(self):
        assert self._status < 3
        assert self._status >= 0
        self._status = self._status + 1

    def __decrease_status(self):
        assert self._status < 3
        assert self._status > 0
        self._status = self._status - 1

    def get_hit_by(self, ball):
        self._get_hit_by.append(ball)
        self.__increase_status()

        # Remove active hit
        rescue = '0'
        if len(self._active_hit) > 0:
            rescue = self._active_hit.pop(0)

        return rescue

