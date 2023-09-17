
class Timer():
    def __init__(self):
        self.timer=3599
        self.start=True
        self.sleep = 1
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.date = "00:00:00"
    def format_date(self,numb):
        if numb < 60:
            self.second = numb
        else:
            self.second = numb % 60
            self.minute = numb // 60
            if self.minute > 59:
                self.hour = numb // (60 * 60)
                self.minute = int( numb // 60 % 60)

        self.date = "{}:{}:{}".format(self.hour, self.minute, self.second)
        return self.date
    def get_hour(self):
        print('bla')
        return self.hour
    def show_time(self):
        print(self.date)
        return self.date    