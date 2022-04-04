##################################################################################
##################################################################################
#### In this example we create a simple GUI to read the UID of an RFID card   ####
#### We are using the PyGObject library.                                      ####
##################################################################################
##################################################################################


import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk, GLib
from puzzle1 import Rfid
import threading

class Window(Gtk.Window):
    def __init__(self):
        # Create the window widget
        super().__init__(title="RFID reader")

        # Box where widgets will be contained
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)     # Create the box widget
        self.add(box)                                                       # Add the box widget to the window
        self.set_border_width(10)                                           # Set some space for inner widgets

        # Label widget
        self.label = Gtk.Label()                                            # Create the label
        self.label.set_name("first-label")                                  # Set an ID to the label
        self.label.set_text("Please, login with your university card")      # Set the inital text to the label
        self.label.set_size_request(400,100)                                # Set the minimum size of the widget
        box.add(self.label)                                                 # Add the label to the box

        # Button widget
        self.button = Gtk.Button(label = "Clear")                           # Create the button widget
        self.button.set_sensitive(False)                                    # Set the button not abailable for click
        self.button.connect("clicked", self.reset)                          # Connect the button to the function reset
        box.pack_start(self.button, True, True, 0)                          # Add button to the box

        self.nfc_reader = Rfid()                                            # Create the Rfid object from puzzle 1
        self.start_thread()                                                 # Call function to start threating

    # Update label Function
    def update_label(self):
        self.label.set_name("second-label")                                 # Set a new ID for the label
        self.label.set_text("UID:" + self.uid)                              # Set the new text displayed on the label
        self.button.set_sensitive(True)                                     # Set the button abailable for click

    # Reset function
    def reset(self, button):
        self.label.set_name("first-label")                                  # Set the initial ID to the label
        self.label.set_text("Please, login with your university card")      # Set the initial text to the label
        self.button.set_sensitive(False)                                    # Set the button not abailable for click
        self.start_thread()                                                 # Start a new thread

    # Thread function    
    def start_thread(self):
        thread = threading.Thread(target=self.scan_uid)                     # Create a thread
        thread.setDaemon(True)                                              # Set Daemon mode so the thread can die
        thread.start()                                                      # Start the thread

    # Read UID function
    def scan_uid(self):
        self.uid = self.nfc_reader.read_uid()                               # Set the UID value
        GLib.idle_add(self.update_label)                                    # Creates the function to update the label



# Main function
if __name__ == "__main__":
    # Style provider set up
    style_provider = Gtk.CssProvider()                                      # Create a provider where we will get the style
    style_provider.load_from_path('style.css')                              # Set the path to the css file
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(), style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    # Create the window
    win = Window()                                                          # Call the window function
    win.connect("destroy", Gtk.main_quit)                                   # Connect the window to the cross button to stop the script
    win.show_all()                                                          # Show all widgets created on the windows object
    Gtk.main()                                                              # Create a loop for the scipt to run