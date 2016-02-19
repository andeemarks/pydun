from domain import Location, Map
import subprocess
from display import Display
from Tkinter import Tk

root = Tk()


class CommandHandler:
    def __init__(self):
        """Not much happens here just yet"""

    def process_command(self, command):
        """"React to command"""
        print command
        if (command == 'open'):
            display.show_location(locations['entrance'])

        if (command == 'exit'):
            global root
            root.quit
            root.destroy

        if (command == 'look'):
            display.show("""There's an old book on the ground.  It shakes violently.  You want to open it, but your instinct tells you to leave it""")

        # if (command == 'open'):
        #     display.show("""You are swallowed whole by the book.  The end""")

        # if (command == 'look'):
        #     display.show("""The title reads 'The Book of Life'""")

        # if (command == 'open'):
        #     display.show("""You are swallowed whole by the book.  The end""")

# music.kill()

locations = Location.bootstrap()
map = Map()

# music = subprocess.Popen(["afplay", "./soundtrack.mp3"])

command_handler = CommandHandler()
display = Display(root, command_handler)
current_location = map.start()
display.show_location(current_location)

root.mainloop()

