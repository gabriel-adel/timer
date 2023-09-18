
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
    def get_timer(self):
        return self.timer
    def set_second(self,modify):
        self.second = modify
    def set_minute(self,modify):
        self.minute = modify
    def set_hour(self,modify):
        self.hour = modify
    def set_date(self, modify):
        self.date 
    def format_date(self):
        if self.get_timer() < 59:
            self.set_second(self.get_timer())
        else:
            self.set_second(self.get_timer() % 60)
            self.set_minute(self.get_timer() // 60)
            if self.minute > 59:
                self.set_minute(self.get_timer() // 60 % 60)
                self.set_hour(self.get_timer() // (60 * 60))
        
        self.date = "{}:{}:{}".format(self.hour, self.minute, self.second)
        return self.get_date()
    def add_timer(self,accress  = 1):
        self.timer = self.get_timer() + accress
        return  self.get_timer()   
    
    def get_hour(self):
        return self.hour
    def get_minute(self):
        return self.minute
    def get_second(self):
        return self.second
    def show_time(self):
        return self.date    