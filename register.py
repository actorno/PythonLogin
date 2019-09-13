from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


class Register(Screen):
    def do_register(self, nameText, emailText, passwordText):
        app = App.get_running_app()

        app.username = nameText
        app.email = emailText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'

        app.config.read(app.get_application_config())
        app.config.write()

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
