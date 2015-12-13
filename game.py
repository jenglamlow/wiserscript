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

        return self._team[ball_team].get_status(ball_num)

    def process(self, action):
        # Check whether is foul or attack
        if len(action) == 4:
            # Attack
            striker = action[:2]
            target = action[2:]
            striker_team = striker[0]
            target_team = target[0]

            # Check whether the striker is contesting ball
            if (Game.get_ball_status(self, striker) != 0):
                print ('"' + striker + '" is not contesting ball')
                return False

            # Check whether the target is eliminated
            if (Game.get_ball_status(self, target) == 3):
                print ('"' + target + '" is already eliminated')
                return False

            # Miss Hit?
            if striker_team != target_team:
                self._team[striker_team].update_status(action)
                self._team[target_team].update_status(action)
            else:
                print (striker + " Miss Hit " + target)
                self._team[striker_team].update_status(action)

            self._sequence.append(action)

        return True
