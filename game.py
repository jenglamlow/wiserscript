from team import Team
from tabulate import tabulate


class Game:

    @property
    def sequence(self):
        return self._sequence

    @property
    def seq_num(self):
        return self._seq_num

    @property
    def team(self):
        return self._team

    @seq_num.setter
    def seq_num(self, value):
        self._seq_num = value

    def __init__(self, name):
        self.name = name
        self._seq_num = 1
        self._sequence = []
        self._team = {'r': Team('r'), 'w': Team('w')}
        self._debug_mode = False

        print ("Game Name:", name)

    def activate_debug(self):
        self._debug_mode = True

    def print_info(self):
        # Constuct Table
        table = []
        team_list = ['r', 'w']

        for team in team_list:
            for i in range(0, 7):
                row = []
                row.append("%s%d" % (team, (i + 1)))
                row.append(self._team[team].ball[i].status)

                row.append(", ".join(self._team[team].ball[i].
                           get_hit_list))
                row.append(", ".join(self._team[team].ball[i].
                           active_hit_list))
                row.append(", ".join(self._team[team]._pending_hit))
                row.append(", ".join(self._team[team]._pending_miss_hit))

                table.append(row)

        print (tabulate(table,
               headers=["Ball", "Stat", "Get Hit", "Hit",
                        "Pending", "Miss Hit"],
               tablefmt="psql", numalign="center", stralign="center"))

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

        return self._team[rescue_team].ball[rescue_ball-1].rescue()

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

            # Check whether the target is eliminated
            if self.is_eliminated(target):
                raise ValueError("\"%s\" is already eliminated" % (target))

            # Check whether the striker is contesting ball
            if not self.is_contesting(striker):
                if self.is_eliminated(striker):
                    raise ValueError("\"%s\" is already eliminated" %
                                     (striker))
                else:
                    raise ValueError("\"%s\" is not contesting ball" %
                                     (striker))

            # Proper Hit
            if striker_team != target_team:
                print (striker + " Hit " + target)
                self._team[striker_team].ball[striker_num - 1].hit(target)
                rescue_ball = self._team[target_team].ball[target_num - 1] \
                    .get_hit_by(striker)

                # Check any pending hit list for eliminated ball
                if (self.is_eliminated(target)):
                    # Remove Active Hit List from Striker
                    print (target + " Eliminated")
                    self._team[striker_team].ball[striker_num - 1] \
                        .remove_all_active_hit(target)

                    # Keep track pending hit list
                    self._team[target_team].update_pending_hit(target_num)

                # if there is a rescue ball
                if rescue_ball != '0':
                    print (rescue_ball + " Rescued")
                    self.rescue(rescue_ball)
                else:
                    # Check any pending rescue list
                    rescue_ball = self._team[target_team].get_pending_rescue()

                    if rescue_ball != '0':
                        print (rescue_ball + " Rescued")
                        get_hit = self.rescue(rescue_ball)
                        get_hit_team = get_hit[0]
                        get_hit_num = int(get_hit[1])
                        self._team[get_hit_team].ball[get_hit_num-1] \
                            .remove_active_hit(rescue_ball)

            # Miss Hit
            else:
                print (striker + " Miss Hit " + target)
                print (striker + " Eliminated")
                self._team[striker_team].ball[striker_num - 1].miss_hit(target)
                self._team[target_team].ball[target_num - 1] \
                    .get_hit_by(striker)

                self._team[target_team].update_pending_hit(striker_num)

                if target_team == 'w':
                    opponent = 'r'
                else:
                    opponent = 'w'

                self._team[opponent].update_pending_miss_hit(target)

            self._sequence.append(action)
            if self._debug_mode:
                self.print_info()
                print("")
