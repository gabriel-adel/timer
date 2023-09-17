from timer import Timer
import time
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='ola mundo')
timer = Timer()
aa=3599
sleep = 1
start = True
timer.timerWork()
MyApp().run()
while start:
    #  logica vai ficara qui
    res = timer.format_date(aa)
    print(res)
    aa+=1
    time.sleep(sleep)
    
    if aa >= 25200:
        start = False