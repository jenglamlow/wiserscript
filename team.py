from ball import Ball


class Team:

    @property
    def ball(self):
        return self._ball

    def __init__(self, color):
        self._color = color
        self._ball = []
        self._pending_hit = []
        self._pending_miss_hit = []

        for i in range(1, 8):
            self._ball.append(Ball(i))

    def reset(self):
        self._pending_hit = []
        self._pending_miss_hit = []
        for i in range(0, 7):
            self._ball[i].reset()

    def get_status(self, num):
        return self._ball[num - 1].status

    def update_pending_hit(self, num):
        if len(self._ball[num-1].active_hit_list) > 0:
            self._pending_hit.extend(self._ball[num-1].active_hit_list)

    def update_pending_miss_hit(self, ball):
        self._pending_miss_hit.append(ball)

    def get_pending_rescue(self):
        pending_rescue = '0'

        # Save hit list first
        while True:
            if len(self._pending_hit) > 0:
                pending_rescue = self._pending_hit.pop(0)
                break

            if len(self._pending_miss_hit) > 0:
                pending_rescue = self._pending_miss_hit.pop(0)
                break
            break

        return pending_rescue
