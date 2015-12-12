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

    def get_ball_status(self, ball):
        ball_team = ball[0]
        ball_num = int(ball[1])

        return self._team[ball_team].ball[ball_num - 1].status


    def add_action(self, action):
        # Check whether is foul or attack
        if len(action) == 4:
            # Attack
            # striker_team = action[0]
            # striker_num = int(action[1])
            # target_team = action[2]
            # target_num = int(action[3])
            striker = action[:2]

            # Check whether the ball is contesting ball
            if (Game.get_ball_status(self, striker) != 0):
                print ('"' + striker + '" is not contesting ball')
                return False
            self._sequence.append(action)

        return True