from colors import red
import utility
from domain import Location

print red("PYDUN - A Python Dungeon-Styled Text Adventure!\n")
print red("(Type 'help' for commands.)\n")

locations = Location.bootstrap()

locations['start'].show()

# TODO Make utility.get_command() force the user to enter a valid command
# TODO Hint: https://wiki.python.org/moin/WhileLoop
command = utility.get_command()

if (command == 'help'):
    utility.list_commands()

if (command == 'open'):
    locations['entrance'].show()

    command = utility.get_command()

if (command == 'look'):
    utility.show("""There's an old book on the ground.  It shakes violently.
        You want to open it, but your instinct tells you to leave it""")
    command = utility.get_command()

if (command == 'open'):
    utility.show("""You are swallowed whole by the book.  The end""")

if (command == 'look'):
    utility.show("""The title reads 'The Book of Life'""")
    command = utility.get_command()

if (command == 'open'):
    utility.show("""You are swallowed whole by the book.  The end""")

print red("\nThanks for playing!")
