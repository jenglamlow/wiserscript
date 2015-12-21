class Ball:

    @property
    def number(self):
        return self._number

    @property
    def status(self):
        return self._status

    @property
    def active_hit_list(self):
        return self._active_hit_list

    @property
    def get_hit_list(self):
        return self._get_hit_list

    @property
    def hit_list(self):
        return self._hit_list

    @property
    def foul(self):
        return self._foul

    def __init__(self, number):
        self._number = number
        self._status = 0
        self._foul = 0
        self._miss_hit = False
        self._hit_list = []
        self._get_hit_list = []
        self._active_hit_list = []

    def reset(self):
        self._status = 0
        self._foul = 0
        self._miss_hit = False
        self._hit_list = []
        self._get_hit_list = []
        self._active_hit_list = []

    def __increase_status(self):
        assert self._status < 3
        assert self._status >= 0
        self._status = self._status + 1

    def __decrease_status(self):
        assert self._status < 3
        assert self._status > 0
        self._status = self._status - 1

    def get_hit_by(self, ball):
        self._get_hit_list.append(ball)
        self.__increase_status()

        # Remove active hit
        rescue = '0'
        if len(self._active_hit_list) > 0:
            rescue = self._active_hit_list.pop(0)

        return rescue

    def remove_all_active_hit(self, ball):
        count = self._active_hit_list.count(ball)
        for i in range(0, count):
            self._active_hit_list.remove(ball)

    def remove_active_hit(self, ball):
        if self._active_hit_list.count(ball) > 0:
            self._active_hit_list.remove(ball)

    def hit(self, ball):
        self._hit_list.append(ball)
        self._active_hit_list.append(ball)

    def miss_hit(self, ball):
        self.miss_hit = True
        self._status = 3

        # To be confirm
        self.hit(ball)

    def rescue(self):
        self.__decrease_status()
        return self._get_hit_list.pop(0)

    def commit_foul(self):
        self._foul = self._foul + 1
