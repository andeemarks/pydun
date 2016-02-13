from colors import red, green, blue
import utility
import string
from domain import Location

print red("PYDUN - A Python Dungeon-Styled Text Adventure!\n") 
print red("(Type 'help' for commands.)\n")

utility.show("""You are standing at the front of an old two-story house.  The gate swings open
with a long sad creak and beckons you insde.  As you walk up the front path, you feel the windows of the house staring at you... Was that a
flutter of movement behind the upstairs curtain?  Regardless, you continue
walking until you arrive at the front door.""")

command = string.lower (utility.get_command())

if (command == 'help'):     
	utility.list_commands()

if (command == 'open'):     
	utility.show("""With a hefty shove, the front door swings slowly inwards, and you
cough as dust tickles your throat.  You gulp and take a nervous step inside.
No sooner have you crossed the threshold than the old front door slams shut
behind you, locking you in.  Resisting the temptation to scream, you wait in
the hallway as your eyes slowly adjust to the gloom.""")

	command = utility.get_command()
	# TODO: (1) If the player looks now, they'll find an old book on the ground
	# TODO: Hint: http://www.pythonforbeginners.com/basics/python-conditional-statements
	# TODO: (2) If the player enters "Help" or "help" or "HELP" (or any other variation of commands),
	# TODO: they should be treated the same way.
	# TODO: Hint: https://docs.python.org/2/library/string.html#string-functions

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
