class Ball:

    @property
    def number(self):
        return self._number

    @property
    def status(self):
        return self._status
    

    def __init__(self, number):
        self._number = number
        self._status = 0
        self._foul = 0
        self._hit_record = []
        self._get_hit_by = []
        self._active_hit = []

    def hit(ball):
        pass
