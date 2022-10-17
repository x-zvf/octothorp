from email.mime import application
import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio

MENU_XML="""
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="app-menu">
    <section>
      <item>
        <attribute name="action">win.about</attribute>
        <attribute name="label" translatable="yes">_About</attribute>
      </item>
      <item>
        <attribute name="action">win.quit</attribute>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="accel">&lt;Primary&gt;Q</attribute>
    </item>
    </section>
  </menu>
</interface>
"""


class Header(Gtk.HeaderBar):
    def __init__(self) -> None:
        super().__init__()
        self.menu_button = Gtk.MenuButton()
        self.menu_button.set_icon_name("open-menu-symbolic")
        self.menu = Gtk.Builder.new_from_string(MENU_XML, -1).get_object("app-menu")
        self.menu_button.set_menu_model(self.menu)
        self.pack_end(self.menu_button)


        self.add_button = Gtk.Button()
        self.add_button.set_icon_name("list-add-symbolic")
        self.add_button.set_tooltip_text("Add new OTP")
        self.pack_start(self.add_button)

        
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(350, 400)
        self.set_title("pyOTP")

        self.quit_action = Gio.SimpleAction.new("quit", None) # look at MENU_XML win.quit
        self.quit_action.connect("activate", self.on_close)
        self.add_action(self.quit_action) # (self window) == win in MENU_XML
        
        self.about_action = Gio.SimpleAction.new("about", None) # look at MENU_XML win.about
        self.about_action.connect("activate", self.on_about)
        self.add_action(self.about_action) # (self window) == win in MENU_XML

        self.header = Header()
        self.set_titlebar(self.header)
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.button = Gtk.Button(label="Hello")
        self.box1.append(self.button)
        self.button.connect('clicked', lambda x,y: print(x,y))

    def on_close(self, action, param):
        pass

    def on_about(self, action, param):
        about_window = Adw.AboutWindow(
            transient_for=self,
            modal=True,
            application_name="pyOTP",
            developer_name = "Péter Bohner (xzvf)",
            copyright = "Copyright 2022 Péter Bohner (aka. xzvf)",
            )
        about_window.present()


        

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
    

def run():
    app = MyApp(application_id="me.bohner.pyotp")
    app.run(sys.argv)
