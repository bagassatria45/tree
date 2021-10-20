#!/usr/bin/python3
import kivy

from kivy.app import App

from kivy.lang import Builder

kivy.require('1.9.1')

kvfile = Builder.load_string("""
Label:
	text:
		('[b]Hello[/b] [color = ff0099]World[/color]\n'
		'[color = ff0099]Hello[/color] [b]World[/b]\n'
		'[b]Hello[/b] [color = ff0099]World:):)[/color]')
	markup: True
	font_size: '64pt'
""")

class kvfileApp(App):
    def build(self):
        return kvfile

kv = kvfileApp()
kv.run()