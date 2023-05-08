import kivy
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from datetime import timedelta
from time import time, sleep, strftime, gmtime, mktime
import threading


# frontend design file .kv
file = "mytimer.kv"
Builder.load_file(file)


class TimerGrid(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = 1  # state of timer 
        self.tic = 0  # time of pressing the start button
        self.timer = 0  # if timer is running
        self.time_total = 0  # total time when timer is running

    def start(self):
        """
        Pressing the start button
        Starting the time loop
        """
        self.state = 1
        threading.Thread(target=self.time_loop).start()

    def stop(self):
        """
        Pressing stop button - timer pausing
        setting state to 0 and saving total time
        """
        self.state = 0
        self.time_total = self.timer

    def reset(self):
        """
        Reset button - resteting timer
        """
        self.ids.clock.text = '0:00:00'
        self.state = 1
        self.timer = 0
        self.tic = 0
        self.time_total = 0

    def time_loop(self):
        """
        Time loop function running while state == 1
        """
        self.tic = time()

        while self.state:
            self.timer = self.time_total + time() - self.tic
            self.ids.clock.text = str(timedelta(seconds=int(self.timer)))
            sleep(.99999)

class MyApp(App):
    def build(self):
        return TimerGrid()


if __name__ == '__main__':
    MyApp().run()
