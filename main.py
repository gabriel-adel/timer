from timer import Timer
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__()
        self.timer = Timer()
    def build(self):
        self.label = Label(text=f"Tempo: {self.timer.get_date()}")
        Clock.schedule_interval(self.update_label,1)
        return self.label
    def update_label(self, dt):
        self.label.text = f"Tempo: {self.get_current_time()}"
        self.timer.add_timer()
    def get_current_time(self):
        return self.timer.format_date()
         
        
# timer = Timer()
# sleep = 1
# start = True
# timer = Timer()
if __name__ == '__main__':
    MyApp().run()
# while start:
#     #  logica vai ficara qui
#     res = timer.format_date()
#     timeRet = timer.add_timer()
#     time.sleep(sleep)
#     print(res)
    
#     if timeRet >= 25200:
#         start = False