from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from connected import Connected
from register import Register


class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def do_register(self):
        app = App.get_running_app()

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'register'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


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
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def resetForm(self):
        self.ids['name'].text = ""
        self.ids['email'].text = ""
        self.ids['password'].text = ""


class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Register(name='register'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == '__main__':
    LoginApp().run()
