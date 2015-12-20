from team import Team


class Game:

    @property
    def sequence(self):
        return self._sequence

    @property
    def seq_num(self):
        return self._seq_num

    @seq_num.setter
    def seq_num(self, value):
        self._seq_num = value

    def __init__(self, name):
        self.name = name
        self._seq_num = 1
        self._sequence = []
        self._team = {'r': Team('r'), 'w': Team('w')}

        print ("Game Name:", name)

    def print_info(self):
        for i in range(0, 7):
            print ("r%d:" % (i + 1), self._team['r'].ball[i].status,
                   self._team['r'].ball[i].active_hit_list)

        for i in range(0, 7):
            print ("w%d:" % (i + 1), self._team['w'].ball[i].status,
                   self._team['w'].ball[i].active_hit_list)

    def get_ball_status(self, ball):
        ball_team = ball[0]
        ball_num = int(ball[1])

        return self._team[ball_team].get_status(ball_num)

    def is_contesting(self, ball):
        return self.get_ball_status(ball) == 0

    def is_first_lock(self, ball):
        return self.get_ball_status(ball) == 1

    def is_second_lock(self, ball):
        return self.get_ball_status(ball) == 2

    def is_eliminated(self, ball):
        return self.get_ball_status(ball) == 3

    def rescue(self, ball):
        rescue_team = ball[0]
        rescue_ball = int(ball[1])

        self._team[rescue_team].ball[rescue_ball-1].rescue()

    def reset(self):
        self._seq_num = 1
        self._sequence = []
        self._team['r'].reset()
        self._team['w'].reset()

    def process(self, action):
        # Check whether is foul or attack
        if len(action) == 4:
            # Attack
            striker = action[:2]
            target = action[2:]
            striker_team = striker[0]
            target_team = target[0]
            striker_num = int(striker[1])
            target_num = int(target[1])

            # Check whether the striker is contesting ball
            if (not self.is_contesting(striker)):
                print ("\"%s\" is not contesting ball" % (striker))
                return False

            # Check whether the target is eliminated
            if (self.is_eliminated(target)):
                print ("\"%s\" is already eliminated" % (target))
                return False

            # Proper Hit
            if striker_team != target_team:
                self._team[striker_team].ball[striker_num - 1].hit(target)
                rescue_ball = self._team[target_team].ball[target_num - 1] \
                    .get_hit_by(striker)

                if rescue_ball != '0':
                    self.rescue(rescue_ball)
                else:
                    # Check any pending rescue list
                    rescue_ball = self._team[target_team].get_pending_rescue()

                    if rescue_ball != '0':
                        self.rescue(rescue_ball)

                # Check any pending hit list for eliminated ball
                if (self.is_eliminated(target)):
                    # Remove Active Hit List from Striker
                    self._team[striker_team].ball[striker_num - 1].remove_all_active_hit(target)

                    # Keep track pending hit list
                    self._team[target_team].update_pending_hit(target_num)

            # Miss Hit
            else:
                print (striker + " Miss Hit " + target)

            self._sequence.append(action)

        return True
