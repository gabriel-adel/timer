
class Timer():
    def __init__(self):
        self.timer=3590
        self.start=True
        self.sleep = 1
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.date = "00:00:00"
        
    def get_date(self):
        return self.date
    def format_date(self):
        if self.timer < 60:
            self.second = self.timer
        else:
            self.second = self.timer % 60
            self.minute = self.timer // 60
            if self.minute > 59:
                self.hour = self.timer // (60 * 60)
                self.minute = int( self.timer // 60 % 60)
        self.date = "{}:{}:{}".format(self.hour, self.minute, self.second)
        return self.get_date()
    def add_timer(self,accress  = 1):
        self.timer = self.timer + accress
        return  self.timer   
    
    def get_hour(self):
        return self.hour
    def get_minute(self):
        return self.minute
    def get_second(self):
        return self.second
    def show_time(self):
        return self.date    