#!/usr/bin/python3
from kivy.app import App
from kivy.uix.button import Button

class TestKivy(App):
    def build(self):
        return Button(text='Hello World!')


TestKivy().run()