from colors import blue
import utility


class Map(object):
    def __init__(self):
        """Initialise the map of the dungeon"""
        self.locations = Location.bootstrap()

    def start(self):
        """Return the first location for the dungeon"""
        return self.locations['start']

    def move_from(self, location, command):
        """Return the destination after taking 'command' from 'location'"""
        return location


class Location(object):
    def __init__(self, description):
        """Create a new Location with this description"""

        self.description = description
        self.destinations = []
        self.commands = ['open', 'look', 'help', 'quit']

    def show(self):
        """Print my description"""

        utility.show(self.description)

    def show_commands(self):
        print blue("\nYou have the following commands available:")
        for command in self.commands:
            print blue("- " + command)

    @staticmethod
    def bootstrap():
        """Create a set of Locations with descriptions"""

        start = Location("""You are standing at the front of an old two-story house.  The gate
swings open with a long sad creak and beckons you insde.  As you walk
up the front path, you feel the windows of the house staring at
you... Was that a flutter of movement behind the upstairs curtain?
Regardless, you continue walking until you arrive at the front
door.""")

        entrance = Location("""With a hefty shove, the front door swings slowly inwards,
and you cough as dust tickles your throat.  You gulp and take a nervous step
inside. No sooner have you crossed the threshold than the old front door slams
shut behind you, locking you in.  Resisting the temptation to scream, you wait
in the hallway as your eyes slowly adjust to the gloom.""")

        map = {}
        map[1, 1] = start
        map[1, 2] = entrance

        return {'start': start, 'entrance': entrance}
