from colors import red, green, blue
import utility
import string
from domain import Location

print red("PYDUN - A Python Dungeon-Styled Text Adventure!\n") 
print red("(Type 'help' for commands.)\n")

locations = Location.bootstrap()

locations['start'].show()

command = utility.get_command()

if (command == 'help'):     
	utility.list_commands()

if (command == 'open'):     
	locations['entrance'].show()

	command = utility.get_command()

if (command == 'look'):
	utility.show("""There's an old book on the ground.  It shakes violently.  You want to open it, but your instinct tells you to leave it""")
	command = utility.get_command()

if (command == 'open'):
	utility.show("""You are swallowed whole by the book.  The end""")

if (command == 'look'):
	utility.show("""The title reads 'The Book of Life'""")
	command = utility.get_command()

if (command == 'open'):
	utility.show("""You are swallowed whole by the book.  The end""")

print red("\nThanks for playing!")
