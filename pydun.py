from colors import red, green, blue
import utility

print red("PYDUN - A Python Dungeon-Styled Text Adventure!\n") 
print red("(Type 'help' for commands.)\n")

utility.show("""You are standing at the front of an old two-story house.  The gate swings open
with a long sad creak and beckons you inside.  As you walk up the front path, you feel the windows of the house staring at you... Was that a
flutter of movement behind the upstairs curtain?  Regardless, you continue
walking until you arrive at the front door.""")

command = utility.get_command()

if (command == 'help'):     
	utility.list_commands()

if (command == 'open'):     
	utility.show("""With a hefty shove, the front door swings slowly inwards, and you
cough as dust tickles your throat.  You gulp and take a nervous step inside.
No sooner have you crossed the threshold than the old front door slams shut
behind you, locking you in.  Resisting the temptation to scream, you wait in
the hallway as your eyes slowly adjust to the gloom.""")

	command = utility.get_command()

	# TODO
	# TODO: If the player looks now, they'll find an old book on the ground
	# TODO

if (command == 'look'):
	utility.show("""You peer closely at the front door, but apart from it's obvious strength and age, it appears normal.""")

print red("\nThanks for playing!")
