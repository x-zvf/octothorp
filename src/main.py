import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(250, 400)
        self.set_title("pyOTP")
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.button = Gtk.Button(label="Hello")
        self.box1.append(self.button)
        self.button.connect('clicked', lambda x,y: print(x,y))

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)

        self.win.present()

app = MyApp(application_id="me.bohner.pyotp")
app.run(sys.argv)
