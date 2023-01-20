WORK_INTERVAL = 5
REST_INTERVAL = 2
lONG_REST_INTERVAL = 6

class Pomodoro():
    def __init__(self):
        self.number_of_tik = 1
        self.round_number = 1
        self.round_length = WORK_INTERVAL
        self.tik_number = 0
        self.check_mark = ''
        self.NUMBER_OF_WORK_ROUND = 2
        self.NUMBER_OF_REST_ROUND = 1

    def next_round(self):
        self.round_number += 1
        if self.round_number % 2 != 0:
            self.round_length = WORK_INTERVAL
        elif self.round_number == self.NUMBER_OF_REST_ROUND + self.NUMBER_OF_WORK_ROUND+1:
            self.round_length = lONG_REST_INTERVAL

        else:
            self.round_length = REST_INTERVAL

    def increase_tik(self):
        self.check_mark += '✓'



    def round_is_on(self):
        self.round_length -= 1
        if self.round_length == -1:
            self.next_round()
            return False
        return True

    def convert_to_min(self):
        min = self.round_length // 60
        sec = self.round_length % 60
        min_d = min // 10
        min_y = min % 10
        sec_d = sec // 10
        sec_y = sec % 10
        return f'{min_d}{min_y}:{sec_d}{sec_y}'

    def reset(self):
        self.check_mark = ''
        self.round_number = 1
        self.round_length = WORK_INTERVAL
