from timer import Timer
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window
class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__()
        self.screen_width = 0
        self.screen_height = 0
        self.timer = Timer()
        pass
    def build(self):
        
        self.screen_width, self.screen_height = Window.size
        Clock.schedule_interval(self.update_label, 1)
        return self.root
    def update_label(self,dt):
        self.timer.format_date()
        horas = self.root.ids.horas
        horas.text = f"Tempo: {self.get_date()}"
        self.timer.add_timer()
    def get_width(self):
        return self.screen_width
    def get_height(self):
        return self.screen_height
    def get_date(self):
        return self.timer.get_date()
    def button_callback(self):
        print('bla')
        
if __name__ == '__main__':
    app = MyApp()
    app.run()