from timer import Timer
from kivy.clock import Clock
from kivy.app import App
from db import Db
# ainda preciso arrumar os botoes mas por enquanto vou deixar assim
class Screen(App):
    def __init__(self):
        super(Screen, self).__init__()
        self.timer = Timer()
        self.start = False
        db = Db()
        db.connection()
        sql = 'create table bla(id int not null)'
        db.create_table(sql)
    def build(self):
        Clock.schedule_interval(self.update_label, 1)
        return self.root
    def update_label(self,dt):
        self.timer.format_date()
        horas = self.root.ids.horas
        horas.text = f"Tempo: {self.get_date()}"
        if self.start:
            self.timer.add_timer()
    
    def button_start(self):
        self.start = True
    def get_date(self):
        return self.timer.get_date()
    def button_pause(self):
        self.start = False
    def button_stop(self):
        self.start = False
        self.timer.zera_time()