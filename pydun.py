from domain import Location, Map
import subprocess
from display import Display
from Tkinter import Tk

locations = Location.bootstrap()
map = Map()

# music = subprocess.Popen(["afplay", "./soundtrack.mp3"])

root = Tk()
display = Display(root)
current_location = map.start()
display.show(current_location)

root.mainloop()


# if (command == 'open'):
#     locations['entrance'].show()

#     command = utility.get_command()

# if (command == 'look'):
#     utility.show("""There's an old book on the ground.  It shakes violently.
# You want to open it, but your instinct tells you to leave it""")
#     command = utility.get_command()

# if (command == 'open'):
#     utility.show("""You are swallowed whole by the book.  The end""")

# if (command == 'look'):
#     utility.show("""The title reads 'The Book of Life'""")
#     command = utility.get_command()

# if (command == 'open'):
#     utility.show("""You are swallowed whole by the book.  The end""")

# music.kill()
