from colors import red
from domain import Location, Map
import utility
import subprocess

print red("PYDUN - A Python Dungeon-Styled Text Adventure!\n")
print red("(Type 'help' for commands.)\n")

locations = Location.bootstrap()
map = Map()

music = subprocess.Popen(["afplay", "./soundtrack.mp3"])

map.start().show()

command = utility.get_command()
while command != 'quit':
    if (command == 'help'):
        locations['start'].show_commands()
        
    command = utility.get_command()


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

print red("\nThanks for playing!")

music.kill()
