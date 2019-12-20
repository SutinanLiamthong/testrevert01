from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        #update
        self.submit = Button(text ='Sign In')
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.pressed)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()

