import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window

#Set the app size
Window.size =(500,700)
#Designate Out  .kv dsigne file
Builder.load_file('my.kv')

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # Set columns
        self.cols = 1

        # Add widgets
        self.add_widget(Label(text="Name:"))
        # Add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text="Favorite:"))
        # Add input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Create submit button
        self.submit = Button(text="submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        # print(f"Hello: {name}, you like pizza {pizza}")
        # priny on screen
        self.add_widget(Label(text=f"Hello: {name}, you like pizza {pizza}"))

        # clear input box
        self.pizza.text = ""
        self.name.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
